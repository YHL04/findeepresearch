

import requests

from api_keys import api_key


def search_sec_filings(query, api_key, from_=0, size=50, sort=[{"filedAt": {"order": "desc"}}]):
    """
    Searches for SEC filings using the sec-api.io API.

    Parameters:
    - query (str): The search query in Lucene syntax (e.g., "formType:\"10-K\" AND ticker:AAPL").
    - api_key (str): Your sec-api.io API key.
    - from_ (int): The starting position for pagination (default: 0).
    - size (int): The number of filings to return per request (default: 50, max: 50).
    - sort (list): A list of sorting criteria (default: sort by filedAt in descending order).

    Returns:
    - dict: The JSON response from the API, or None if an error occurs.
    """
    url = "https://api.sec-api.io"
    payload = {
        "query": query,
        "from": str(from_),
        "size": str(size),
        "sort": sort
    }
    headers = {
        "Authorization": api_key
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    # Replace 'YOUR_API_KEY' with your actual API key from sec-api.io
    query = "formType:\"10-K\" AND ticker:AAPL"  # Find the most recent 10-K filing for Apple (AAPL)
    result = search_sec_filings(query, api_key, size=1)  # Retrieve only 1 result

    if result is None:
        print("Error occurred while fetching data.")
    elif "filings" in result and len(result["filings"]) > 0:
        filing = result["filings"][0]
        print(f"Accession Number: {filing['accessionNo']}")
        print(f"Form Type: {filing['formType']}")
        print(f"Filed At: {filing['filedAt']}")
        print(f"Ticker: {filing['ticker']}")
        print(f"CIK: {filing['cik']}")
        print(f"Company Name: {filing['companyName']}")
    else:
        print("No filings found.")