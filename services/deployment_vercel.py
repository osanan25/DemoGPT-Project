import requests
from decouple import config
import json, base64

VERCEL_API_TOKEN = config("VERCEL_API_TOKEN")


def deploy_html_to_vercel(frontend_code, deployment_name):
    VERCEL_DEPLOY_API_URL = "https://api.vercel.com/v11/now/deployments"

    # Headers including Vercel API token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {VERCEL_API_TOKEN}",
    }

    encoded_html_content = base64.b64encode(frontend_code.encode("utf-8")).decode(
        "utf-8"
    )

    # Payload for deploying the HTML content
    deployment_payload = {
        "name": deployment_name,
        "files": [
            {
                "data": encoded_html_content,
                "encoding": "base64",
                "file": "index.html",
            }
        ],
    }

    try:
        # Make the API request to deploy the HTML content
        response = requests.post(
            VERCEL_DEPLOY_API_URL,
            data=json.dumps(deployment_payload),
            headers=headers,
        )
        response.raise_for_status()  # Raise HTTPError for bad responses

        deployment_response = response.json()
        deployment_id = deployment_response.get("id")
        deploy_url = deployment_response.get("alias")[0]

        # Print the response
        return {"deployment_id": deployment_id, "deploy_url": deploy_url}
    except requests.exceptions.RequestException as e:
        # Handle request-related errors
        return {"error": f"Request error: {e}"}
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors
        return {"error": f"JSON decoding error: {e}"}
    except Exception as e:
        # Handle other unexpected errors
        return {"error": f"An unexpected error occurred: {e}"}


def delete_deployment(deployment_id):
    VERCEL_DEPLOY_API_URL = "https://api.vercel.com/v11/now/deployments"
    # Your Vercel API token
    VERCEL_API_TOKEN = "your-vercel-api-token"

    # Headers including Vercel API token
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {VERCEL_API_TOKEN}",
    }

    try:
        # Make the API request to delete the deployment
        delete_response = requests.delete(
            f"{VERCEL_DEPLOY_API_URL}/{deployment_id}",
            headers=headers,
        )

        # Raise an exception for bad status codes
        delete_response.raise_for_status()

        # Return the JSON response
        return delete_response.json()
    except requests.exceptions.HTTPError as errh:
        # Handle HTTP errors
        return {
            "error": f"HTTP Error: {errh}",
            "status_code": delete_response.status_code,
        }
    except requests.exceptions.RequestException as err:
        # Handle other types of errors
        return {"error": f"Request Exception: {err}"}


# print(deploy_html_to_vercel(frontend_code=html_content))
# {'accountId': 'team_DhTwoCs5shRaCMmK4mBQvYXu', 'alias': [{'configuredBy': 'A', 'configuredChangedAt': 1705583086687, 'createdAt': 1705583086687, 'deployment': None, 'domain': 'test-project-jade-seven.vercel.app', 'environment': 'production', 'target': 'PRODUCTION'}], 'autoExposeSystemEnvs': True, 'autoAssignCustomDomains': True, 'autoAssignCustomDomainsUpdatedBy': 'system', 'buildCommand': None, 'createdAt': 1705583086687, 'devCommand': None, 'directoryListing': False, 'framework': None, 'gitForkProtection': True, 'id': 'prj_3GIv8TTe50LiDKfCjn4WDtMj7x4z', 'installCommand': None, 'name': 'test-project', 'nodeVersion': '18.x', 'outputDirectory': None, 'publicSource': None, 'rootDirectory': None, 'serverlessFunctionRegion': 'iad1', 'sourceFilesOutsideRootDirectory': True, 'ssoProtection': {'deploymentType': 'prod_deployment_urls_and_all_previews'}, 'updatedAt': 1705583086687, 'live': False, 'gitComments': {'onCommit': False, 'onPullRequest': True}, 'latestDeployments': [], 'targets': {}}


# import requests
# import json

# # Vercel API endpoint for creating projects
# VERCEL_API_URL = "https://api.vercel.com/v1/projects"

# # Your Vercel API token
# VERCEL_API_TOKEN = "ZxSdhd9qF32H2UjYopZGC6iP"

# # Headers including Vercel API token
# headers = {
#     "Content-Type": "application/json",
#     "Authorization": f"Bearer {VERCEL_API_TOKEN}",
# }

# # Payload for creating a project
# project_payload = {
#     "name": "test-project",
# }

# # Make the API request to create the project
# response = requests.post(
#     VERCEL_API_URL,
#     data=json.dumps(project_payload),
#     headers=headers,
# )

# # Print the response
# print(response.json())

# # -----------------------------------------redeploy-------------------------------------------------

# update_payload = {
#     "files": [
#         {
#             "data": encoded_html_content,
#             "encoding": "base64",
#             "file": "index.html",
#         }
#     ],
# }

# # Replace 'your-deployment-name' and '3Xgf8RxpKzeT7xoharXFkqFAnbLB' with your actual deployment name and ID
# deployment_url = "https://vercel.com/sanjeev-s-projects-b92aa3b1/your-deployment-name/3Xgf8RxpKzeT7xoharXFkqFAnbLB"

# # Make the API request to update the deployment
# update_response = requests.post(
#     deployment_url,
#     data=json.dumps(update_payload),
#     headers=headers,
# )

# # Print the response
# print(update_response.json())

# -----------------------------------delete deployment---------------------------------------------------------
