# Rock vs Mine Prediction

This project predicts whether a given sonar signal is reflected from a **rock** or a **mine** using machine learning.  
It is based on the **Sonar Dataset** from the UCI Machine Learning Repository.

## 📂 Project Structure
```
.
├── Rock vs Mine predict..ipynb   # Jupyter Notebook containing code & training
├── sonar data.csv                # Dataset file
├── README.md                     # Project documentation
├── requirements.txt              # Required Python libraries
├── run.py                         # Python script for CLI prediction
```

## 📊 Dataset
The dataset (`sonar data.csv`) contains **60 numerical features** representing sonar signal strengths at different frequencies.  
- **R** → Rock  
- **M** → Mine  

Source: [UCI Sonar Dataset](https://archive.ics.uci.edu/ml/datasets/connectionist+bench+(sonar,+mines+vs.+rocks))

## ⚙️ How it Works
1. **Load Dataset** – Reads the sonar CSV file into a Pandas DataFrame.
2. **Data Preprocessing** – Separates features and labels, normalizes data.
3. **Model Training** – Uses **Logistic Regression** for classification.
4. **Evaluation** – Measures accuracy on training and testing sets.
5. **Prediction** – Allows manual input to predict Rock or Mine.

## 🚀 Installation & Usage
### 1. Clone the Repository
```bash
git clone https://github.com/your-username/rock-vs-mine-prediction.git
cd rock-vs-mine-prediction
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Notebook
```bash
jupyter notebook "Rock vs Mine predict..ipynb"
```

### 4. Run the CLI Script
```bash
python run.py
```

## 🧠 Model Details
- **Algorithm**: Logistic Regression
- **Accuracy**: ~83% on test data (may vary)
- **Features**: 60 numerical features from sonar readings

## 📌 Requirements
See [`requirements.txt`](requirements.txt) for exact dependencies.

## 📜 License
This project is licensed under the MIT License – feel free to use and modify.
