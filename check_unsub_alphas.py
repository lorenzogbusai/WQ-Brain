import sys
from main import WQSession

API_URL = "https://api.worldquantbrain.com/users/self/alphas?limit=100&offset=0&status=UNSUBMITTED%1FIS_FAIL&order=is.sharpe&hidden=false"

def check_unsubmitted_alphas():
    codes = []
    wq = WQSession()
    response = wq.get(API_URL)
    try:
        data = response.json()
    except Exception as e:
        sys.exit(f"Error decoding JSON: {e}")

    results = data.get('results', [])
    if not results:
        print("No unsubmitted alphas found.")
        return

    print(f"Found {len(results)} unsubmitted alphas:")
    for alpha in results:
        alpha_id = alpha.get('id', 'Unknown ID')
        # Retrieve the alpha code if available (as seen in scrape_alphas.py)
        code = alpha.get('regular', {}).get('code', 'No code available')
        codes += [code]
    return codes

if __name__ == "__main__":
    check_unsubmitted_alphas()