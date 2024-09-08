def solution(video_len, pos, op_start, op_end, commands):
    # 분으로 변경
    times = [video_len, pos, op_start, op_end]
    times = [int(t[:2]) * 60 + int(t[3:]) for t in times]  # 각 시간을 분으로 변환
    video_len, pos, op_start, op_end = times  # 변환된 값을 다시 각 변수에 할당
    
    for command in commands:
        # 오프닝 사이에 있을 때
        if op_start<=pos<=op_end:
            pos = op_end
            
        # prev 누를 때
        if command == "prev":
            if pos<10:
                pos = 0
            else:
                pos -= 10
        
        if command == "next":
            if pos+10>video_len:
                pos = video_len
            else:
                pos += 10
    
    if op_start<=pos<=op_end:
        pos = op_end
    
    # 시간을 다시 "MM:SS" 형식으로 변환
    minutes = pos // 60
    seconds = pos % 60
    return f"{minutes:02d}:{seconds:02d}"  # :02d를 사용해 두 자리로 맞춤