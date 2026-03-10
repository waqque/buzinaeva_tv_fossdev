def calculate_ndfl(income):
    """Прогрессивная шкала НДФЛ по РФ."""
    if income <= 0:
        return 0
    
    tiers = [
        (2_400_000, 0.13, 0),           # до 2.4млн: 13%
        (5_000_000, 0.15, 312_000),     # 2.4-5млн: 312к + 15%
        (20_000_000, 0.18, 702_000),    # 5-20млн: 702к + 18%
        (50_000_000, 0.20, 3_402_000),  # 20-50млн: 3.402млн + 20%
        (float('inf'), 0.22, 9_402_000) # >50млн: 9.402млн + 22%
    ]
    
    tax = 0
    prev_limit = 0
    
    for limit, rate, base_tax in tiers:
        if income > prev_limit:
            taxable = min(income, limit) - prev_limit
            tax += taxable * rate
        prev_limit = limit
    
    return round(tax) 
