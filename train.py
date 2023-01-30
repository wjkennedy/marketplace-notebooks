import pandas as pd
from jira import JIRA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


jira = JIRA(oauth={
    'access_token': 'your_access_token',
        'access_token_secret': 'your


# Connect to Jira
#jira = JIRA(basic_auth=('username', 'password'), options={'server': 'https://yourserver.com'})

# Search for issues
issues = jira.search_issues("project = 'your_project_key'", maxResults=1000)

# Create a list to store the data
data = []

# Extract the text, labels and keys from the issues
for issue in issues:
    text = issue.fields.summary + ' ' + issue.fields.description
        labels = issue.fields.customfield_your_label_field
            key = issue.key
                data.append({'text': text, 'labels': labels, 'key': key})

                # Create a dataframe from the list
                df = pd.DataFrame(data)

                # Split the dataset into training and test sets
                X_train, X_test, y_train, y_test = train_test_split(df['text'], df['labels'], test_size=0.2)

                # Create a pipeline with a TfidfVectorizer and a LogisticRegression
                pipeline = Pipeline([
                    ('tfidf', TfidfVectorizer()),
                        ('clf', LogisticRegression())
                        ])

                        # Fit the pipeline to the training data
                        pipeline.fit(X_train, y_train)

                        # Make predictions on the test set
                        y_pred = pipeline.predict(X_test)

                        # Print the classification report
                        print(classification_report(y_test, y_pred))

                        # Save the model to a file
                        import joblib
                        joblib.dump(pipeline, 'model.pkl')

