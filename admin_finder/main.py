import requests, sys, logging
from concurrent.futures import ThreadPoolExecutor
from colorama import Fore as f
import pyuseragents as agent

def set_logger(logger_name, log_file):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger

def get_user_agent():
    return agent.random()

def check_subdomain(url, subdomain, found_logger, not_found_logger):
    headers = {'User-Agent': get_user_agent()}
    request = f'https://{subdomain}.{url}'
    try:
        http = requests.get(request, timeout=10, headers=headers)
        http.raise_for_status()  
        if http.status_code == 200:
            result = f.GREEN + f'[ + ] SUBDOMAIN FOUND - {request}'
            found_logger.info(result)
            return result
        else:
            result = f.RED + f'[ - ] SUBDOMAIN NOT FOUND - {request}'
            not_found_logger.info(result)
            return None
    except requests.RequestException as e:
        result = f.RED + f'[ - ] REQUEST ERROR - {request}: {e}'
        not_found_logger.error(result)
        return None
    except Exception as e:
        result = f.RED + f'[ - ] UNKNOWN ERROR - {request}: {e}'
        not_found_logger.error(result)
        return None


def check_page(url, line, found_logger, not_found_logger):
    headers = {'User-Agent': get_user_agent()}
    request = f'{url}/{line}'
    try:
        http = requests.get(request, timeout=10, headers=headers)
        http.raise_for_status()  
        if http.status_code == 200 and b'Page not found... ' not in http.content:
            result = f.GREEN + f'[ + ] PAGE FOUND - {request}'
            found_logger.info(result)
            return result
        else:
            result = f.RED + f'[ - ] PAGE NOT FOUND - {request}'
            not_found_logger.info(result)
            return None
    except requests.RequestException as e:
        result = f.RED + f'[ - ] REQUEST ERROR - {request}: {e}'
        not_found_logger.error(result)
        return None
    except Exception as e:
        result = f.RED + f'[ - ] UNKNOWN ERROR - {request}: {e}'
        not_found_logger.error(result)
        return None

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python main.py <URL> <file_path> <subdomains_file> <mode: subdomains/links>")
        sys.exit(1)

    url = sys.argv[1]
    lives = []

    found_logger = set_logger('found_logger', 'found.log')
    not_found_logger = set_logger('not_found_logger', 'not_found.log')

    mode = sys.argv[4]

    with ThreadPoolExecutor(max_workers=10) as executor:
        if mode == 'subdomains':
            print("Running in 'subdomains' mode...")
            with open(sys.argv[3], 'r') as sub_file:
                subdomains = [line.strip() for line in sub_file]
                print("Checking Subdomains (might take a while)")
            results = list(executor.map(lambda sub: check_subdomain(url, sub, found_logger, not_found_logger), subdomains))
        elif mode == 'links':
            print("Running in 'links' mode...")
            with open(sys.argv[2], 'r') as arq:
                lines = [line.strip() for line in arq]
                print(f"Checking Links (might take a while)")
            results = list(executor.map(lambda line: check_page(url, line, found_logger, not_found_logger), lines))
        else:
            print("Invalid mode selected. Choose 'subdomains' or 'links'.")
            sys.exit(1)

        for result in results:
            if result:
                print(result)
                lives.append(result.split(' - ')[-1])

    print('FINISHED')
