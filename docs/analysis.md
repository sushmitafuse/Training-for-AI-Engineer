# Problem analysis for ABC Travels and Tours Pvt. Ltd

## 1. User Story

As a traveller, I want good recommendations and accomodation at an affordable price so that I can have a better travelling experience.

As an admin, I want to provide appropriate travelling packages to the customer on the basis of their interest and previous engagement so that our customers are satisfied with our services.


## 2. Solution and Problem formulation

   **a. What is the problem?**

We need this new system to make our travel packages appealing to the customers. We also want to improve package recommendations from customer feedback for better user experience. Our system will classify the user emotions learned from customer feedback which is trained on customer feedback data. 

Assumption in our system would be:

- All the customer will give honest feedback after using our services 
- The emotion of the customer fall within the seven class of classification
- The specific words used in feedback matter to the model

Other similar problems would be classifying emotion of user’s comment and feedback on 
	E-commerce platform to understand customer satisfaction.

**b. Why does the problem need to be solved?**

Our system can provide personalized applications to the customer which will improve customer satisfaction. It will help to retain old customers and add new ones which gives competitive advantage among other competitors. It can help to develop attractive marketing strategies with accommodation of recommendations.

**c. How would I solve the problem?**

The problem can be solved manually by reading the comments on our social media and feedback comments on our e-commerce website. We can review the feedback submitted to us by the customers after the visit.

Using ML tools, we can use a transfer learning approach for better system performance. We will be using pre trained transformer based model BERT and fine-tune the model on our dataset so that our approach has good generalization and better performance.


## 3. Data

   **a. What data they have that might be related, in any way?**

   They have manually labeled some of the dataset from the comments of the facebook page and the reviews on their website. The data consists of 7445 sentences containing 7 types of emotions(classes).
    

	
**b. Do we have enough data?**

The data provided is enough for using the traditional machine learning classification approaches. As the trend is moving towards using deep learning, the data is not enough to train a deep learning model from scratch. One workaround would be to use the pretrained transformer based model like BERT and fine-tune the model on our dataset so that our approach has good generalization. By looking at the performance metric of our approaches using available data, we can later decide if additional data are necessary. 

 **c. How helpful is the nature of available data? What might be the ideal nature of the data?**

The available data is quite good because it is balanced and it contains more variations (like long as well as short sentences). The ideal nature of the data would be such that it will represent most of the review/feedback encountered in the real world so that our model will not be biased towards a particular type of sentence.

**d. How can we collect more quality data?**

If more data is required, we can collect some data from manual labeling by the staff. We can also use crowdsourcing marketplace like Mechanical Turk to generate more data. 

**e. How can we access their data if that is available?**

Currently, their labeled data is stored in an excel file so it is easy to access the data for analysis. 

**f. What is their current data infrastructure and data handling process? How they stored and manipulated data right now?**

Currently, they are using web scraping to collect all the reviews from the facebook page and website and each sentence is stored in a row in an excel file. The labeling of the sentences is done manually by the staff.

**g. Do they have internal data-dedicated teams? If they have what are their roles and responsibilities?**

As their team is small, they do not have internal data-dedicated teams.

**h. What can be the other external/internal source of data than can be used?**

We can also check if data related to similar projects(emotion detection and sentiment analysis) are available on different platforms like kaggle.

## 4. Performance metrics

Since the ISEAR dataset we are using has seven classes of emotion with an almost balanced number of instances for each class therefore accuracy metric can be used as the performance metric for our purpose. Beside that various metrics that are derived from the confusion matrix can also be used to support accuracy. For example metrics  such as Precision, Recall, F1 score, Sensitivity, Specificity, Positive Predictive Value(PPV) etc can be used.