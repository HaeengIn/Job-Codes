def get_monthly_budget():
    while True:
        try:
            budget = float(input("한 달 예산을 입력해주세요 (숫자만): "))
            if budget > 0:
                return budget
            else:
                print("예산은 0보다 커야 합니다. 다시 입력해주세요.")
        except ValueError:
            print("잘못된 입력입니다. 숫자만 입력해주세요.")

def get_daily_expenses(days_to_track):
    expenses = []
    print(f"\n{days_to_track}일 동안의 일일 지출을 입력해주세요.")
    for day in range(1, days_to_track + 1):
        while True:
            try:
                expense = float(input(f"{day}일차 지출: "))
                if expense >= 0:
                    expenses.append(expense)
                    break
                else:
                    print("지출은 0 이상이어야 합니다. 다시 입력해주세요.")
            except ValueError:
                print("잘못된 입력입니다. 숫자만 입력해주세요.")
    return expenses

def analyze_and_forecast(expenses, monthly_budget):
    if not expenses:
        print("입력된 지출 내역이 없습니다.")
        return

    days_tracked = len(expenses)
    total_spent = sum(expenses)
    average_daily_spending = total_spent / days_tracked
    forecasted_monthly_spending = average_daily_spending * 30

    print("\n--- 지출 분석 및 예측 결과 ---")
    print(f"추적 기간: {days_tracked}일")
    print(f"총 지출: {total_spent:,.0f}원")
    print(f"일 평균 지출: {average_daily_spending:,.0f}원")
    print(f"월간 예상 지출 (30일 기준): {forecasted_monthly_spending:,.0f}원")
    print(f"설정한 월간 예산: {monthly_budget:,.0f}원")

    if forecasted_monthly_spending > monthly_budget:
        overspent_amount = forecasted_monthly_spending - monthly_budget
        print(f"\n[경고] 이 소비 패턴을 유지하면 예산을 {overspent_amount:,.0f}원 초과할 것으로 보입니다.")
        print("지출을 줄이는 것을 고려해보세요.")
    elif forecasted_monthly_spending < monthly_budget * 0.8:
        remaining_amount = monthly_budget - forecasted_monthly_spending
        print(f"\n[안정] 아주 좋습니다! 예산 내에서 안정적으로 소비하고 있습니다.")
        print(f"이대로라면 월말에 약 {remaining_amount:,.0f}원을 아낄 수 있습니다.")
    else:
        remaining_amount = monthly_budget - forecasted_monthly_spending
        print(f"\n[양호] 예산에 맞게 잘 소비하고 있습니다.")
        print(f"이대로라면 월말에 약 {remaining_amount:,.0f}원이 남을 것으로 예상됩니다.")

def main():
    print("--- 일일 지출 패턴 분석 및 월간 지출 예측 프로그램 ---")
    print("최근 지출 내역(수열)을 바탕으로 한 달 지출을 예측하고 분석합니다.\n")

    monthly_budget = get_monthly_budget()

    while True:
        try:
            days_to_track = int(input("\n며칠 동안의 지출을 분석할까요? (예: 7): "))
            if days_to_track > 0:
                break
            else:
                print("분석할 날짜는 1일 이상이어야 합니다.")
        except ValueError:
            print("잘못된 입력입니다. 숫자만 입력해주세요.")

    daily_expenses = get_daily_expenses(days_to_track)
    analyze_and_forecast(daily_expenses, monthly_budget)

    print("\n프로그램을 종료합니다.")

if __name__ == "__main__":
    main()