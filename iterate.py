import csv
import pandas as pd

df = pd.read_csv('issues.csv')

for index, row in df.iterrows():
    issue_key = row['issue_key']
        issue = jira.issue(issue_key)
            comments = jira.comments(issue)
                description = issue.fields.description
                    custom_fields = issue.fields.customfield_12345 # replace 12345 with the ID of the custom field
                        triage_field = issue.fields.customfield_67890 # replace 67890 with the ID of the triage field
                            priority = issue.fields.priority
                                last_comment_date = comments[-1].created
                                    previous_issue_keys = issue.fields.issuelinks

                                           # check if the issue belongs to the correct project
                                               if "keyword1" in comments or "keyword1" in description or "keyword1" in custom_fields:
                                                   print(issue_key + " is in the correct project")
                                                               # update the histogram data
                                                                       histogram_data['correct_project'].append(issue_key)
                                                                   else:
                                                                       print(issue_key + " is NOT in the correct project")
                                                                                           histogram_data['wrong_project'].append(issue_key)

                                                                                                       # check the priority
                                                                                                           if priority == 'High':
                                                                                                               histogram_data['high_priority'].append(issue_key)
                                                                                                           elif priority == 'Medium':
                                                                                                               histogram_data['medium_priority'].append(issue_key)
                                                                                                           else:
                                                                                                               histogram_data['low_priority'].append(issue_key)

                                                                                                                                                       # check the content of the triage field
                                                                                                                                                           if "keyword2" in triage_field:
                                                                                                                                                               histogram_data['triage_keyword'].append(issue_key)
                                                                                                                                                           else:
                                                                                                                                                               histogram_data['no_triage_keyword'].append(issue_key)

                                                                                                                                                                                           # check the date since last comment
                                                                                                                                                                                               current_date = datetime.now()
                                                                                                                                                                                                   date_since_last_comment = current_date - last_comment_date
                                                                                                                                                                                                       if date_since_last_comment.days > 30:
                                                                                                                                                                                                           histogram_data['no_comments_30_days'].append(issue_key)
                                                                                                                                                                                                       else:
                                                                                                                                                                                                           histogram_data['comments_in_30_days'].append(issue_key)

                                                                                                                                                                                                                                       # check previous issue keys
                                                                                                                                                                                                                                           if previous_issue_keys:
                                                                                                                                                                                                                                               histogram_data['has_previous_issue'].append(issue_key)
                                                                                                                                                                                                                                           else:
                                                                                                                                                                                                                                               histogram_data['no_previous_issue'].append(issue_key)

