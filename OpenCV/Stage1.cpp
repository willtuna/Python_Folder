#include <iostream>  
#include <fstream>  
#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  
#include <opencv2/imgproc/imgproc.hpp>  
#include <opencv2/objdetect/objdetect.hpp>  
#include <opencv2/ml/ml.hpp>  
using namespace std;
using namespace cv;

#define PosSamNO 1000    //正樣本個數  1000
#define NegSamNO 16700    //負樣本個數  16700

#define TRAIN false    //true則重新訓練；false則讀取 xml檔
#define CENTRAL_CROP true   //true:训练时，对96*160的INRIA正样本图片剪裁出中间的64*128大小人体  

//HardExample：负样本个数。如果HardExampleNO大于0，表示处理完初始负样本集后，继续处理HardExample负样本集。  
//不使用HardExample时必须设置为0，因为特征向量矩阵和特征类别矩阵的维数初始化时用到这个值  
#define HardExampleNO 0   


//继承自CvSVM的类，因为生成setSVMDetector()中用到的检测子参数时，需要用到训练好的SVM的decision_func参数，  
//但通过查看CvSVM源码可知decision_func参数是protected类型变量，无法直接访问到，只能继承之后通过函数访问  
class MySVM : public CvSVM
{
public:
	//获得SVM的决策函数中的alpha数组  
	double * get_alpha_vector()
	{
		return this->decision_func->alpha;
	}

	//获得SVM的决策函数中的rho参数,即偏移量  
	float get_rho()
	{
		return this->decision_func->rho;
	}
};



int main()
{
	//检测窗口(64,128),块尺寸(16,16),块步长(8,8),cell尺寸(8,8),直方图bin个数9  
	HOGDescriptor hog(Size(64, 128), Size(16, 16), Size(8, 8), Size(8, 8), 9);//HOG检测器，用来计算HOG描述子的  
	int DescriptorDim;//HOG描述子的维数，由图片大小、检测窗口大小、块大小、细胞单元中直方图bin个数决定  
	MySVM svm;//SVM分类器  

	//若TRAIN为true，重新训练分类器  
	if (TRAIN)
	{
		string ImgName;//图片名(绝对路径)  
		ifstream finPos("D:\\INRIAPerson\\INRIAPerson\\96X160H96\\Train\\pos.txt");//正样本图片的文件名列表  
		//ifstream finPos("PersonFromVOC2012List.txt");//正样本图片的文件名列表  
		ifstream finNeg("D:\\INRIAPerson\\INRIAPerson\\Train\\neg_aug.txt");//负样本图片的文件名列表  

		Mat sampleFeatureMat;//所有训练样本的特征向量组成的矩阵，行数等于所有样本的个数，列数等于HOG描述子维数      
		Mat sampleLabelMat;//训练样本的类别向量，行数等于所有样本的个数，列数等于1；1表示有人，-1表示无人  


		//依次读取正样本图片，生成HOG描述子  
		for (int num = 0; num<PosSamNO && getline(finPos, ImgName); num++)
		{
			cout << "Processing Positive Example：" << ImgName << endl;
			//ImgName = "D:\\DataSet\\PersonFromVOC2012\\" + ImgName;//加上正样本的路径名  
			ImgName = "D:\\INRIAPerson\\INRIAPerson\\96X160H96\\Train\\pos\\" + ImgName;//加上正样本的路径名  
			Mat src = imread(ImgName);//读取图片  
			imshow("666", src);
			waitKey(10);
			if (CENTRAL_CROP)
				src = src(Rect(16, 16, 64, 128));//将96*160的INRIA正样本图片剪裁为64*128，即剪去上下左右各16个像素  
			//resize(src,src,Size(64,128));  

			vector<float> descriptors;//HOG描述子向量  
			hog.compute(src, descriptors, Size(8, 8));//计算HOG描述子，检测窗口移动步长(8,8)  
			//cout<<"描述子维数："<<descriptors.size()<<endl;  

			//处理第一个样本时初始化特征向量矩阵和类别矩阵，因为只有知道了特征向量的维数才能初始化特征向量矩阵  
			if (0 == num)
			{
				DescriptorDim = descriptors.size();//HOG描述子的维数  
				//初始化所有训练样本的特征向量组成的矩阵，行数等于所有样本的个数，列数等于HOG描述子维数sampleFeatureMat  
				sampleFeatureMat = Mat::zeros(PosSamNO + NegSamNO + HardExampleNO, DescriptorDim, CV_32FC1);
				//初始化训练样本的类别向量，行数等于所有样本的个数，列数等于1；1表示有人，0表示无人  
				sampleLabelMat = Mat::zeros(PosSamNO + NegSamNO + HardExampleNO, 1, CV_32FC1);
			}

			//将计算好的HOG描述子复制到样本特征矩阵sampleFeatureMat  
			for (int i = 0; i<DescriptorDim; i++)
				sampleFeatureMat.at<float>(num, i) = descriptors[i];//第num个样本的特征向量中的第i个元素  
			sampleLabelMat.at<float>(num, 0) = 1;//正样本类别为1，有人  
		}

		//依次读取负样本图片，生成HOG描述子  
		for (int num = 0; num<NegSamNO && getline(finNeg, ImgName); num++)
		{
			cout << "Processing Negative Example：" << ImgName << endl;
			ImgName = "D:\\INRIAPerson\\INRIAPerson\\Train\\neg_Aug\\" + ImgName;//加上负样本的路径名  
			Mat src = imread(ImgName);//读取图片  
			imshow("666", src);
			waitKey(10);
			

			vector<float> descriptors;//HOG描述子向量  
			hog.compute(src, descriptors, Size(8, 8));//计算HOG描述子，检测窗口移动步长(8,8)  
			//cout<<"描述子维数："<<descriptors.size()<<endl;  

			//将计算好的HOG描述子复制到样本特征矩阵sampleFeatureMat  
			for (int i = 0; i<DescriptorDim; i++)
				sampleFeatureMat.at<float>(num + PosSamNO, i) = descriptors[i];//第PosSamNO+num个样本的特征向量中的第i个元素  
			sampleLabelMat.at<float>(num + PosSamNO, 0) = -1;//负样本类别为-1，无人  
		}
		
		//处理HardExample负样本  
		if (HardExampleNO > 0)
		{
			ifstream finHardExample("D:\\INRIAPerson\\INRIAPerson\\Train\\neg.txt");//HardExample负样本的文件名列表  
			//依次读取HardExample负样本图片，生成HOG描述子  
			for (int num = 0; num<HardExampleNO && getline(finHardExample, ImgName); num++)
			{
				cout << "Processing Hard Example：" << ImgName << endl;
				ImgName = "D:\\INRIAPerson\\INRIAPerson\\Train\\neg\\" + ImgName;//加上HardExample负样本的路径名  
				Mat src = imread(ImgName);//读取图片  
				//resize(src,img,Size(64,128));  

				vector<float> descriptors;//HOG描述子向量  
				hog.compute(src, descriptors, Size(8, 8));//计算HOG描述子，检测窗口移动步长(8,8)  
				//cout<<"描述子维数："<<descriptors.size()<<endl;  

				//将计算好的HOG描述子复制到样本特征矩阵sampleFeatureMat  
				for (int i = 0; i<DescriptorDim; i++)
					sampleFeatureMat.at<float>(num + PosSamNO + NegSamNO, i) = descriptors[i];//第PosSamNO+num个样本的特征向量中的第i个元素  
				sampleLabelMat.at<float>(num + PosSamNO + NegSamNO, 0) = -1;//负样本类别为-1，无人  
			}
		}
		
		////输出样本的HOG特征向量矩阵到文件  
		//ofstream fout("SampleFeatureMat.txt");  
		//for(int i=0; i<PosSamNO+NegSamNO; i++)  
		//{  
		//  fout<<i<<endl;  
		//  for(int j=0; j<DescriptorDim; j++)  
		//      fout<<sampleFeatureMat.at<float>(i,j)<<"  ";  
		//  fout<<endl;  
		//}  

		//训练SVM分类器  
		//迭代终止条件，当迭代满1000次或误差小于FLT_EPSILON时停止迭代  
		CvTermCriteria criteria = cvTermCriteria(CV_TERMCRIT_ITER + CV_TERMCRIT_EPS, 1000, FLT_EPSILON);
		//SVM参数：SVM类型为C_SVC；线性核函数；松弛因子C=0.01  
		CvSVMParams param(CvSVM::C_SVC, CvSVM::LINEAR, 0, 1, 0, 0.01, 0, 0, 0, criteria);
		cout << "開始訓練SVM分類器" << endl;
		svm.train(sampleFeatureMat, sampleLabelMat, Mat(), Mat(), param);//训练分类器  
		cout << "訓練完成" << endl;
		svm.save("SVM_HOG.xml");//將訓練好的SVM模型保存為xml文件  

	}
	else //若TRAIN为false，從XML文件讀取訓練好的分類器  
	{
		svm.load("SVM_HOG.xml");//從XML文件讀取訓練好的SVM模型  
	}


	/*************************************************************************************************
	线性SVM训练完成后得到的XML文件里面，有一个数组，叫做support vector，还有一个数组，叫做alpha,有一个浮点数，叫做rho;
	将alpha矩阵同support vector相乘，注意，alpha*supportVector,将得到一个列向量。之后，再该列向量的最后添加一个元素rho。
	如此，变得到了一个分类器，利用该分类器，直接替换opencv中行人检测默认的那个分类器（cv::HOGDescriptor::setSVMDetector()），
	就可以利用你的训练样本训练出来的分类器进行行人检测了。
	***************************************************************************************************/
	DescriptorDim = svm.get_var_count();//特征向量的维数，即HOG描述子的维数  
	int supportVectorNum = svm.get_support_vector_count();//支持向量的个数  
	cout << "支持向量個數：" << supportVectorNum << endl;

	Mat alphaMat = Mat::zeros(1, supportVectorNum, CV_32FC1);//alpha向量，长度等于支持向量个数  
	Mat supportVectorMat = Mat::zeros(supportVectorNum, DescriptorDim, CV_32FC1);//支持向量矩阵  
	Mat resultMat = Mat::zeros(1, DescriptorDim, CV_32FC1);//alpha向量乘以支持向量矩阵的结果  

	//将支持向量的数据复制到supportVectorMat矩阵中  
	for (int i = 0; i<supportVectorNum; i++)
	{
		const float * pSVData = svm.get_support_vector(i);//返回第i个支持向量的数据指针  
		for (int j = 0; j<DescriptorDim; j++)
		{
			//cout<<pData[j]<<" ";  
			supportVectorMat.at<float>(i, j) = pSVData[j];
		}
	}

	//将alpha向量的数据复制到alphaMat中  
	double * pAlphaData = svm.get_alpha_vector();//返回SVM的决策函数中的alpha向量  
	for (int i = 0; i<supportVectorNum; i++)
	{
		alphaMat.at<float>(0, i) = pAlphaData[i];
	}

	//计算-(alphaMat * supportVectorMat),结果放到resultMat中  
	//gemm(alphaMat, supportVectorMat, -1, 0, 1, resultMat);//不知道为什么加负号？  
	resultMat = -1 * alphaMat * supportVectorMat;

	//得到最终的setSVMDetector(const vector<float>& detector)参数中可用的检测子  
	vector<float> myDetector;
	//将resultMat中的数据复制到数组myDetector中  
	for (int i = 0; i<DescriptorDim; i++)
	{
		myDetector.push_back(resultMat.at<float>(0, i));
	}
	//最後添加偏移量rho，得到檢測子 
	myDetector.push_back(svm.get_rho());
	cout << "檢測子維數：" << myDetector.size() << endl;
	//設置HOGDescriptor的檢測子  
	HOGDescriptor myHOG;
	myHOG.setSVMDetector(myDetector);
	//myHOG.setSVMDetector(HOGDescriptor::getDefaultPeopleDetector());  

	//保存檢測子參數到文件  
	ofstream fout("HOGDetectorForOpenCV.txt");
	for (int i = 0; i<myDetector.size(); i++)
	{
		fout << myDetector[i] << endl;
	}


	/************** 讀入圖片進行HOG行人檢測 ******************/
	
	Mat src = imread("C:\\Users\\a8512\\Desktop\\b.png");
	vector<Rect> found, found_filtered;//矩形框數组  
	cout << "進行多尺度HOG人體檢測" << endl;
	myHOG.detectMultiScale(src, found, 0, Size(8, 8), Size(32, 32), 1.03, 2); //對圖片進行多尺度行人檢測  
	cout << "找到的矩形框個數：" << found.size() << endl;

	//找出所有没有嵌套的矩形框r,並放入found_filtered中,如果有嵌套的话,則取外面最大的那個矩形框放入found_filtered中  
	for (int i = 0; i < found.size(); i++)
	{
		Rect r = found[i];
		int j = 0;
		for (; j < found.size(); j++)
			if (j != i && (r & found[j]) == r)
				break;
		if (j == found.size())
			found_filtered.push_back(r);
	}

	//劃出矩形框，因為hog檢測出的矩形框比實際人體框要稍微大些,所以這裡需要做一些調整  
	for (int i = 0; i<found_filtered.size(); i++)
	{
		Rect r = found_filtered[i];
		r.x += cvRound(r.width*0.1);
		r.width = cvRound(r.width*0.8);
		r.y += cvRound(r.height*0.07);
		r.height = cvRound(r.height*0.8);
		rectangle(src, r.tl(), r.br(), Scalar(0, 255, 0), 2);
	}

	imwrite("ImgProcessed.jpg", src);
	namedWindow("src", 0);
	imshow("src", src);
	waitKey();

	system("pause");
}
