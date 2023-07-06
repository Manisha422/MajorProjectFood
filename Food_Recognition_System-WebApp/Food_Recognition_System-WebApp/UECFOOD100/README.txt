<<<"UEC FOOD 100": 100-kind food dataset (release 1.0)>>>

The dataset "UEC FOOD 100" contains 100-kind food photos, each of which 
has a bounding box indicating the location of the food item in the photo.

Most of the food categories in this dataset are popular foods in Japan. 
Therefore, some catarogies might not be familiar with other people than
Japanese. 

This dataset was built to implement a practical food recognition system 
which is intend to be used in Japan. In fact, we have released a real-time
100-kind food recognition application for Android smartphones. You can 
get to know the detail and download an APK file from http://foodcam.mobi/ .

This ZIP file contains the following files:

  [1-100]        :  directory names correspond to food ID.
  [1-100]/*.jpg  :  food photo files (some photos are duplicated in two or
                    more directories, since they includes two or more food items.)
  [1-100]/bb_info.txt:  bounding box information for the photo files in each directory

  category.txt    : food list including the correspondences between food
                    IDs and food names in English
  category_ja_{euc,utf8.sjis}.txt : food list including the correspondences 
                    between food IDs and food names in Japanese
  multiple_food.txt: the list representing food photos including two or 
                    more food items

If you publish a paper using our food dataset, we'd glad if you could refer to 
the following paper:

Y. Matsuda and K. Yanai: Multiple-Food Recognition Considering
Co-occurrence Employing Manifold Ranking, IAPR International
Conference on Pattern Recognition (ICPR), pp.2017-2020 (2012).

@InProceedings{mats12,
  author="Matsuda, Y. and Yanai, K.",
  title="Multiple-Food Recognition Considering Co-occurrence Employing
Manifold Ranking",
  booktitle="Proc. of IAPR International Conference on Pattern
Recognition (ICPR)",
  pages="2017--2020",
  year="2012",
}

The best performance for 100-class food classification given the
bounding box information was 51.9 %. 
This result is described in the following paper.

Y. Kawano and K. Yanai: Rapid Mobile Food Recognition using Fisher
Vector, Asian Conference on Pattern Recognition, (2013/11).

@InProceedings{kawa11,
  author="Kawano, Y. and Yanai, K.",
  title="Rapid Mobile Food Recognition using Fisher Vector",
  booktitle="Proc. of Asian Conference on Pattern Recognition",
  year="2013/11",
  memo="http://foodcam.mobi/"
}

If you have comments and questions, please feel free to send e-mail 
to the following address:
  food-group@mm.cs.uec.ac.jp

------------ 
Contact:

Food Recognition Research Group:
  Kawano Yoshiyuki (Master Student)
  Prof. Keiji Yanai

  food-group@mm.cs.uec.ac.jp

Department of Informatics, 
The University of Electro-Communications, Tokyo, Japan
