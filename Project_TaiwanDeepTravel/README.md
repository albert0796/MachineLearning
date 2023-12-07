# Taiwan Deep Travel
### Project Title: Deep Learning-Based Taiwan Travel Destination
### Developer: Cheng-Han Wu, Chi Li
### Advisor: Dr. Yi-Ping Chang
#  
### Complete Report
[Report Link](https://github.com/albert0796/MachineLearning/blob/master/Project_TaiwanDeepTravel/Report/Project%20Description_Open%20Data%20Analysis%20Competition.pdf)
#
### Problem Definition


User
翻成英文: 完整報告
ChatGPT
"Complete Report"

User
幫我精簡以下文句，架構維持一樣，用詞不要太艱深
Taiwan is blessed with beautiful natural and cultural landscapes, and there is a desire to promote Taiwanese attractions through a travel recommendation system that provides travel information tailored to the needs of domestic and international tourists. Additionally, modern life is busy, and people have limited time to search for travel information. If users can input images of their interested destinations into a mobile app, the app can recommend travel destinations that they might like, saving them the time of searching for information online. This app includes two ways of loading images into the model: A. Uploading an image of an interested destination from the device's photo library. B. Instantly capturing images of destinations through the camera function of the mobile app and loading them into the model. The system will utilize deep learning image recognition technology to recognize multiple scenes in real-time and recommend Taiwan travel destination images that are like the recognized scenes, along with detailed information about those destinations.

Contrasting with existing travel recommendation apps on the market, the advantages and features of an image-based travel destination recommendation system are as follows:

Shortcomings of current travel recommendation systems: Most systems rely on users searching for preferred destinations using keywords or tags. However, it can be challenging for users to accurately describe their ideal destinations with limited text and tags, resulting in less precise or overly broad recommendations from the system, which may lack value for users as a reference.
Precisely meeting user needs: Searching and recommending destinations using images, a "search by image" approach, allows for more precise fulfillment of user needs. Images can capture multiple features, eliminating the need for users to input each feature separately for the system to provide recommendations. Moreover, users often struggle to express their ideal scenes in words, making image-based recommendations more aligned with their intentions and better suited to meeting their specific requirements.
Focus on travel destination recommendations: An image-based travel destination recommendation system places emphasis on recommending travel destinations rather than other non-visual tourist experiences. However, for Taiwan, with its abundance of beautiful natural and cultural attractions, scenic appreciation itself is a significant selling point for travel. Therefore, such a recommendation system still holds market value.
Convenient user experience: With the widespread use of mobile devices, developing an app offers a more convenient user experience. Users can easily capture images of their surroundings using the camera function within the recommendation system, allowing the system to recommend Taiwan travel destination images and information that are like the scenes captured in the photos.
ChatGPT
Taiwan boasts stunning natural and cultural landscapes, sparking the idea to enhance tourism through a user-friendly travel recommendation system. Recognizing the time constraints in modern life, the system aims to simplify the process for users, allowing them to input images of desired destinations into a mobile app for tailored travel suggestions. The app offers two convenient ways to load images: A. Uploading from the device's photo library. B. Instantly capturing images through the app's camera function. Utilizing deep learning image recognition, the system identifies real-time scenes, recommending similar Taiwan travel destinations with detailed information.

Contrasting with existing travel apps, the image-based system has key advantages:

Overcoming Current Shortcomings:
Existing systems rely on text-based searches, often resulting in imprecise recommendations. Our approach enables users to precisely meet their needs by searching and recommending destinations through images, eliminating the limitations of text input.

Precise User Fulfillment:
The "search by image" approach ensures more accurate user fulfillment. Images capture multiple features, aligning with users' intentions without the need for detailed text descriptions. This approach resonates better with users who struggle to express their ideal scenes in words.

Focused on Visual Experiences:
Our system emphasizes visual travel destination recommendations, distinguishing itself from other non-visual tourist experiences. Given Taiwan's abundance of scenic attractions, the system adds value by focusing on the appeal of these destinations.

Convenient Mobile Experience:
With the prevalence of mobile devices, our app offers a streamlined user experience. Users can effortlessly capture images using the camera function, allowing the system to recommend Taiwan travel destinations based on scenes captured in the photos.

User
再稍微精簡一點
ChatGPT
Taiwan's captivating landscapes inspire a user-friendly travel recommendation system. Recognizing the time constraints in modern life, the system simplifies the process by allowing users to input images of desired destinations into a mobile app for tailored suggestions. The app offers two convenient ways to load images: A. Uploading from the device's photo library. B. Instantly capturing images through the app's camera function. Using deep learning image recognition, the system identifies real-time scenes, recommending similar Taiwan travel destinations with detailed information.

Contrasting with existing travel apps, the image-based system has key advantages:
*Overcoming Shortcomings:
Existing systems rely on text-based searches, often resulting in imprecise recommendations. Our approach enables users to precisely meet their needs through image-based searches.
*Precise User Fulfillment:
The "search by image" approach ensures accurate user fulfillment, resonating better with users who struggle to express their ideal scenes in words.
*Focused on Visual Experiences:
Our system emphasizes visual travel destination recommendations, adding value by focusing on the appeal of Taiwan's scenic attractions.
*Convenient Mobile Experience:
With the prevalence of mobile devices, our app offers a streamlined user experience. Users can effortlessly capture images using the camera function, allowing the system to recommend Taiwan travel destinations based on scenes captured in the photos.
#  
### Demo  
* [Load an image from the phone's gallery.mp4](https://drive.google.com/file/d/16DuFaOIqSuNrurp-YuRIeEox0RovTAsu/view?usp=drive_link)
* [Capture a photo using the phone.mp4](https://drive.google.com/file/d/12ung4JtLvhvXcfwixREoYPGcFk2teay4/view?usp=drive_link)
#  
### Award 
This project won the [championship](https://github.com/albert0796/MachineLearning/blob/master/Project_TaiwanDeepTravel/Report/%E7%8D%8E%E7%8B%80.png) in [the National College Open Data Artificial Intelligence Competition](http://bigdata.scu.edu.tw/aiads2018/)
#  
### Code
[Open Data Image Conversion 224x224](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/Open%20Data%20%E5%9C%96%E7%89%87%E8%BD%89%20224x224)  
[Traning and Validation Data Preprocessing](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/%E8%A8%93%E7%B7%B4%E5%92%8C%E9%A9%97%E8%AD%89%E8%B3%87%E6%96%99%E9%A0%90%E8%99%95%E7%90%86)  
[Testing Data Augmentation](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/%E6%93%B4%E5%A2%9E%E9%A9%97%E8%AD%89%E8%B3%87%E6%96%99)  
[Model Training](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/%E6%A8%A1%E5%9E%8B%E8%A8%93%E7%B7%B4)  
[Convert the Model's Code To Core ML](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/%E6%A8%A1%E5%9E%8B%E8%BD%89Core%20ML)  
[Recommendation System: Using Cosine Similarity to Recommend the Top 5 Attraction](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/%E9%A4%98%E5%BC%A6%E7%9B%B8%E4%BC%BC%E5%BA%A6%E5%8D%B0%E5%87%BA%E6%9C%80%E7%9B%B8%E4%BC%BC%E7%9A%84%E5%89%8D%E4%BA%94%E5%80%8B%E6%99%AF%E9%BB%9E)  
