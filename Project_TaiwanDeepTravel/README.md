# Taiwan Deep Travel
### 作品名稱: 深度學習為基礎的台灣旅遊景點推薦 APP
### 作者: 吳政翰、李奇
### 指導者: 張揖平 教授
#  
### [詳見完整報告](https://github.com/albert0796/MachineLearning/blob/master/Project_TaiwanDeepTravel/Report/%E7%AB%B6%E8%B3%BD%E6%88%90%E6%9E%9C%E8%AA%AA%E6%98%8E%E6%9B%B8.docx)
### 欲解決之問題與重要性  
台灣富有優美的自然與人文場景，期望藉由旅遊推薦系統推廣台灣景點，提供貼近國內外遊客需求的旅遊資訊。此外，現代人生活忙碌，鮮少有時間搜尋旅遊資訊，倘若用戶能輸入感興趣的景點的影像至手機 APP，APP 就能推薦用戶可能喜歡的旅遊景點，將節省用戶上網查搜查資訊的時間。本 APP 包含兩種載入影像至模型的方式:  A. 從手機裝置的圖庫 (library) 中上傳一張感興趣的景點影像。B. 即時透過手機 APP 的相機功能拍攝景點影像並載入模型。本系統將即時透過深度學習影像辨識技術辨識出影像中多個場景，並依該場景推薦出與其相似的台灣旅遊景點影像，並附加該景點的詳細資訊。  
  
有別於市面上的旅遊推薦系統 APP，影像辨識為基礎的旅遊景點推薦系統的優勢與特點如下：  
* 市面上的旅遊推薦系統缺失：大多是讓用戶以關鍵字或標籤搜尋的方式尋求偏好的景點，然而用戶卻很難以有限的文字與標籤去描述心中理想的景點，導致系統推薦的景點往往不夠精準或過於廣泛，對於用戶而言較缺乏參考價值。  
* 精準滿足用戶需求：以影像進行搜尋與推薦這種「以圖搜圖」的方式更能精準滿足用戶需求。原因在於影像能融合多項特徵，用戶不須繁瑣地輸入每項特徵於系統尋求推薦；再者，用戶往往很難用文字去形容心中理想的場景，因此以影像的表達方式將能更貼近用戶的初衷，系統所推薦的景點也能更精準符合用戶需求。
* 著重於旅遊景點的推薦：影像辨識為基礎的旅遊景點推薦系統會著重於推薦旅遊景點，而非其他不涉及視覺欣賞的觀光體驗。然而對於富含優美自然與人文景點的台灣來說，風景欣賞本身就是台灣旅遊的一大賣點，因此該推薦系統仍具有市場價值。
* 便捷的用戶體驗：鑒於行動裝置的普及，以 APP 的開發形式將能提供更便捷的用戶體驗，其中用戶還能隨手透過推薦系統內的相機功能拍攝周遭感興趣的景點，系統會依照片中的場景推薦出與其相似的台灣旅遊景點影像和資訊。
#  
### 實機展示  
* [DEMO影片_匯入圖片尋求推薦.mp4](https://github.com/albert0796/MachineLearning/blob/master/Project_TaiwanDeepTravel/Report/Open%20Data%20DEMO%E5%BD%B1%E7%89%87_%E5%9C%96%E5%BA%AB.mp4)
* [DEMO影片_拍攝照片尋求推薦.mp4](https://github.com/albert0796/MachineLearning/blob/master/Project_TaiwanDeepTravel/Report/Open%20Data%20DEMO%E5%BD%B1%E7%89%87_%E7%9B%B8%E6%A9%9F.mp4)
#  
### 獲獎紀錄  
該作品參與了於2018年東吳大學主辦的[全國大專院校Open Data人工智能競賽](http://bigdata.scu.edu.tw/aiads2018/)，獲得[第一名](https://github.com/albert0796/MachineLearning/blob/master/Project_TaiwanDeepTravel/Report/%E7%8D%8E%E7%8B%80.png)的佳績。
#  
### 程式碼
[Open Data 圖片轉 224x224](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/Open%20Data%20%E5%9C%96%E7%89%87%E8%BD%89%20224x224)  
[訓練和驗證資料預處理](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/%E8%A8%93%E7%B7%B4%E5%92%8C%E9%A9%97%E8%AD%89%E8%B3%87%E6%96%99%E9%A0%90%E8%99%95%E7%90%86)  
[擴增驗證資料](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/%E6%93%B4%E5%A2%9E%E9%A9%97%E8%AD%89%E8%B3%87%E6%96%99)  
[模型訓練](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/%E6%A8%A1%E5%9E%8B%E8%A8%93%E7%B7%B4)  
[模型轉Core ML](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/%E6%A8%A1%E5%9E%8B%E8%BD%89Core%20ML)  
[餘弦相似度印出最相似的前五個景點](https://github.com/albert0796/MachineLearning/tree/master/Project_TaiwanDeepTravel/Code/%E9%A4%98%E5%BC%A6%E7%9B%B8%E4%BC%BC%E5%BA%A6%E5%8D%B0%E5%87%BA%E6%9C%80%E7%9B%B8%E4%BC%BC%E7%9A%84%E5%89%8D%E4%BA%94%E5%80%8B%E6%99%AF%E9%BB%9E)  
