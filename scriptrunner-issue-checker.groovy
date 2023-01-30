import com.atlassian.jira.component.ComponentAccessor
import com.atlassian.jira.issue.CustomFieldManager
import com.atlassian.jira.issue.Issue
import com.atlassian.jira.issue.comments.CommentManager
import java.time.Duration
import java.time.Instant

// Get the issue by key
def issueKey = "JIRA-123"
def issueManager = ComponentAccessor.issueManager
def issue = issueManager.getIssueObject(issueKey)

// Check the summary and description for keywords
def keywords = ["bug", "error"]
def summary = issue.summary
def description = issue.description
keywords.each { keyword ->
    if (summary.contains(keyword) || description.contains(keyword)) {
        println("Issue contains keyword: " + keyword)
    }
}

// Check the issue type
def issueType = issue.issueType.name
if (issueType != "Bug") {
    println("Issue is not a bug.")
}

// Check the components
def componentManager = ComponentAccessor.componentManager
def components = issue.components
components.each { component ->
    if (component.name != "Frontend") {
        println("Issue is not related to the frontend.")
    }
}

// Check the assignee
def assignee = issue.assignee
if (assignee.name != "John Doe") {
    println("Issue is not assigned to John Doe.")
}

// Check the custom fields
def customFieldManager = ComponentAccessor.customFieldManager
def customField = customFieldManager.getCustomFieldObject("customfield_12345")
def value = issue.getCustomFieldValue(customField)
if (value != "high") {
    println("Issue does not have a high priority.")
}

// Check time since last comment
def commentManager = ComponentAccessor.commentManager
def lastComment = commentManager.getLastComment(issue)
if (lastComment != null) {
    def lastCommentDate = lastComment.created
    def now = Instant.now()
    def timeSinceLastComment = Duration.between(lastCommentDate.toInstant(), now).toDays()
    if (timeSinceLastComment > 7) {
        println("Issue has not had a comment in over 7 days.")
    }
}

// Add a comment to the issue with a summary of the determination
def commentBody = "This issue has been determined to be: "
if (summary.contains("bug") || description.contains("bug")) {
    commentBody += "a bug, "
}
if (issueType == "Bug") {
    commentBody += "of type bug, "
}
if (components.find { component -> component.name == "Frontend" }) {
    commentBody += "related to the frontend, "
}
if (assignee.name == "John Doe") {
    commentBody += "assigned to John Doe, "
}
if (value == "high") {
    commentBody += "with high priority, "
}
if (lastComment != null && timeSinceLastComment > 7

