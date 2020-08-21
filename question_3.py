
sales_team_dict = {}
sales_team_dict['Jordan_belfort'] = {'calls': 178, 'meetings':17,  'sales':6, 'score': score}

score_calls = (sales_team_dict['Jordan_belfort']['calls'])*10
if (sales_team_dict['Jordan_belfort']['calls'])>150:
    score_calls = score_calls + 100

score_meetings = (sales_team_dict['Jordan_belfort']['meetings'])*30
if (sales_team_dict['Jordan_belfort']['meetings'])>20:
    score_meetings = score_meetings + 100

score_sales = (sales_team_dict['Jordan_belfort']['sales'])*100
if (sales_team_dict['Jordan_belfort']['sales'])>20:
    score_sales = score_sales + 100

score = score_calls + score_meetings + score_sales
print(sales_team_dict.items())