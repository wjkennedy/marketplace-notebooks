import groovyx.net.http.HTTPBuilder
import com.atlassian.jira.component.ComponentAccessor

// Issue key
def issueKey = "ABC-123"

// External endpoint URL
def url = "https://example.com/api/issues/${issueKey}"

def http = new HTTPBuilder(url)
def response = http.get() {
    headers.'Content-Type'='application/json'
    response.success = { resp, json ->
    // Un-nest JSON
    def jsonString = json.toString()

    // Get Jira issue
    def issueManager = ComponentAccessor.getIssueManager()
    def issue = issueManager.getIssueObject(issueKey)

    // Add comment to the issue
    issue.commentManager.create(issue.reporter, jsonString)
    println("Comment added with JSON data")
    }
    response.failure = { resp -> 
        println "Error ${resp.statusLine.statusCode} : ${resp.statusLine.reasonPhrase}"
    }
}

