def main():
    # Показать суму простого процентного дохода, используя
    # 0.01 как процентной ставки за период, 10 как количество
    # периодов и $10000 как основную сумму на счете.
    show_interest(rate=0.01, periods=10, principal=10000.0)

def show_interest(principal, rate, periods):
    interest = principal * rate * periods
    print(f'Простой процентный доход составит ${interest:,.2f}')

main()