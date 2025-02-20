import requests

def linkedin_post_agent(text, content, media=False):
    key = 'KEY'
    get_header = {
        'Authorization': 'Bearer {key}'.format(key=key),
    }

    r = requests.get('https://api.linkedin.com/v2/userinfo', headers=get_header)
    di = r.json()
    print(di)
    user_id = di['sub']

    body_text = {
        "author": f"urn:li:person:{user_id}".format(user_id=user_id),
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": {
                "shareCommentary": {
                    "text": "This is my automate API Post"
                },
                "shareMediaCategory": "NONE"
            }
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }

    post_text = requests.post('https://api.linkedin.com/v2/ugcPosts', data=body_text, headers=get_header)
    post_text = post_text.json()
    print(post_text)
