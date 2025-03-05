Crop Recommendation System - Project Description


📌 Introduction

The Crop Recommendation System is a machine learning-based project that suggests the best crop to cultivate based on soil and weather parameters. This helps farmers maximize yield and make informed agricultural decisions.


🔧 Technologies & Tools Used

Programming Language: Python
IDE & Environment: PyCharm, Google Colab

Libraries & Packages:

numpy – For numerical operations
pandas – For data handling and preprocessing
scikit-learn – For machine learning model training
streamlit – For building an interactive web application
matplotlib & seaborn – For data visualization
pickle – For model serialization and deployment

📊 Dataset Details

The dataset consists of various soil nutrients (N, P, K), temperature, humidity, pH level, and rainfall.
The target variable is the recommended crop based on these parameters.
🧠 Machine Learning Model Used
The project uses a Random Forest Classifier, which is an ensemble learning method.

Why Random Forest?

✅ Handles non-linear data well.

✅ Works efficiently with small and large datasets.

✅ Provides high accuracy with low overfitting.

Model Training Steps:

Data Preprocessing:

Checked for missing values.
Normalized feature values.

Feature Selection:

Used correlation analysis to select important features.

Model Training:

Split the data into training and testing sets.
Trained using Random Forest Classifier.
Tuned hyperparameters for better accuracy.

Model Evaluation:

Used accuracy score, precision, recall, and F1-score to evaluate performance.
Achieved good accuracy with balanced precision and recall.

Model Deployment:

Saved the trained model using pickle.
Built a Streamlit web app for easy user interaction.

🌐 Web Application (Using Streamlit)

User Input Fields: Nitrogen (N), Phosphorus (P), Potassium (K), Temperature, Humidity, pH Level, Rainfall.
Prediction Button: On clicking, the system predicts the most suitable crop.

User Interface Enhancements:

Added a homepage with an image.
Created a navigation menu for better user experience.
🚀 Results & Future Enhancements

✅ The model provides accurate crop recommendations based on soil and weather data.

✅ The web application is user-friendly and interactive.

🔹 Future improvements:

Integrating real-time weather data.

Expanding the dataset for better generalization.

Implementing a mobile-friendly version.


![Screenshot (7)](https://github.com/user-attachments/assets/117c765e-0dc1-446d-af69-7aa94e1e95b7)

![Screenshot (8)](https://github.com/user-attachments/assets/45639bb1-2024-41dd-ba8f-7f1fd801eca0)


