def inputBudget():
    while True:
        try:
            print('\n한 달 예산을 입력해주세요.')
            budget = float(input('> '))
            if budget > 0:
                return budget
            else:
                print("예산은 0보다 커야 합니다. 다시 입력해주세요.")
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")

def analyzeExpenses(daysToAnalyze):
    expenses = []
    print(f'\n{daysToAnalyze}일 동안의 지출을 입력해주세요.')
    for day in range(1, daysToAnalyze + 1):
        while True:
            try:
                expense = float(input(f"{day}일차 지출: "))
                if expense >= 0:
                    expenses.append(expense)
                    break
                else:
                    print("지출은 0 이상이어야 합니다. 다시 입력해주세요.")
            except ValueError:
                print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")
    return expenses

def analyze(expenses, budget):
    if not expenses:
        print("입력된 지출 내역이 없습니다.")
        return

    days = len(expenses)
    totalInputExpenses = sum(expenses)
    averageExpenses = totalInputExpenses / days
    """
    등차수열 일반항 공식: a_n = a + (n-1)d
    첫째항: totalInputExpenses
    공차: averageExpenses
    30째 항: a_30 = totalInputExpenses + 29 * averageExpenses
    한 달: 30일

    첫째항 ~ 30째항 모두 더하기: (totalInputExpenses + a_30) / 2
    """
    totalExpenses = (totalInputExpenses + (totalInputExpenses + 29 * averageExpenses)) / 2

    print(f"\n예산: {budget}원")
    print(f'입력한 지출의 일 수: {days}일')
    print(f"총 지출: {totalInputExpenses}원")
    print(f'평균 지출: {averageExpenses}원')
    print(f'월간 예상 지출: {totalExpenses}원')

    if totalExpenses > budget:
        print(f'\n현재 상태: 위험\n월간 예상 지출이 예산을 {totalExpenses - budget}원 초과할 것으로 예상됩니다.\n일일 지출을 줄이는 것을 고려해보세요.')
    elif totalExpenses < budget:
        print(f'\n현재 상태: 양호\n월간 예상 지출이 예산보다 {budget - totalExpenses}원 적을 것으로 예상됩니다.\n현재의 소비 습관을 유지하셔도 좋습니다.')

def main():
    print("--- 일일 지출 패턴 분석 및 월간 지출 예측 프로그램 ---")

    budget = inputBudget()

    while True:
        try:
            print('\n분석할 지출의 일 수를 입력해주세요. (3 이상 7 이하)')
            daysToAnalyze = int(input('> '))
            if 3 <= daysToAnalyze <= 7:
                break
            else:
                print("잘못된 입력입니다. 3 이상 7 이하의 숫자를 입력해주세요.")
        except ValueError:
            print("유효하지 않은 입력입니다. 숫자를 입력해주세요.")

    expenses = analyzeExpenses(daysToAnalyze)
    analyze(expenses, budget)

if __name__ == "__main__":
    main()