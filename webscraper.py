from event_modules.github_search import getGithubSearchResult
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser("event scraper")
    parser.add_argument("website", help="The website from which to get the search result.", type=str)
    args = parser.parse_args()

    # Check for the event
    if args.website == 'github':
        getGithubSearchResult()
    else:
        # If argument equals no event
        print('NO EVENTS FOR', args.website)
    print('END for', args.website)
