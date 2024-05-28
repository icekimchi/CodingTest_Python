def solution(id_list, report, k):
    report_result = {}
    result = {}
    
    #초기값 대입
    for id in id_list:
        report_result[id] = []
        result[id] = 0
    
    #신고 정보 기록
    for reports in report:
        userId, reportId = reports.split()
        if userId in report_result[reportId]:
            continue
        
        report_result[reportId].append(userId)
    
    for reportId in report_result:
        if len(report_result[reportId]) >= k:
            for name in report_result[reportId]:
                result[name] += 1
            
    return list(result.values())
        
    
    