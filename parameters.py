from commands import *
from check_unsub_alphas import check_unsubmitted_alphas


#write a funciton that takes in a funciton from commands retrieves them, checks them agains thte list in chcek_unsub_alphas then build a list DATA
def get_data(func = from_arxiv):
    simulated_alphas = check_unsubmitted_alphas()
    codes = [code for code in func() if code not in simulated_alphas]
    data = []
    for code in codes:
        data.append({
            'neutralization': 'SUBINDUSTRY',
            'decay': 10,
            'truncation': 0.1,
            'delay': 1,
            'universe': 'TOP3000',
            'region': 'USA',
            'code': code
        })
    return data


Data = get_data()