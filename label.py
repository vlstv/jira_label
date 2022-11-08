import os
from jira import JIRA


def update_issue_label(base_url: str, user_email: str, api_token: str, issue: str, label: str) -> None:
 
    jira = JIRA(base_url, basic_auth=(user_email, api_token))
    print(f"Authenticated: {jira}")

    jira_issue = jira.issue(issue)
    print(f"Found issue: {jira_issue}")

    jira_issue.fields.labels.append(label)
    jira_issue.update(fields={"labels": jira_issue.fields.labels})
    print(f"Updated issue: {jira_issue.fields.labels}")

def main():
   print("Starting script")
   # get env vars
   jira_base_url = os.getenv("INPUT_JIRA_URL")
   jira_user_email = os.getenv("INPUT_JIRA_USER")
   jira_api_token = os.getenv("INPUT_JIRA_TOKEN")
   jira_issue= os.getenv("INPUT_JIRA_ISSUE")
   jira_label= os.getenv("INPUT_JIRA_LABEL")
   update_issue_label(jira_base_url, jira_user_email, jira_api_token, jira_issue, jira_label) 
   
if __name__ == '__main__':
    main()
