def calculate_lottery_probability(user_times, max_times):
    """
    计算用户中奖概率

    参数:
    user_times: 用户的时长数据
    max_times: 最大时长数据

    返回:
    用户的中奖概率
    """
    # 对数变换
    log_total_time = math.log(user_times['total_time'] + 1)
    log_control_flight_time = math.log(user_times['control_flight_time'] + 1)
    log_controller_time = math.log(user_times['controller_time'] + 1)

    # 归一化
    norm_total_time = log_total_time / math.log(max_times['max_total_time'])
    norm_control_flight_time = log_control_flight_time / math.log(max_times['max_control_flight_time'])
    norm_controller_time = log_controller_time / math.log(max_times['max_controller_time'])

    # 加权得分计算
    weight_total_time = 0.4
    weight_control_flight_time = 0.6
    weight_controller_time = 0.6

    weighted_score = (norm_total_time * weight_total_time +
                      norm_control_flight_time * weight_control_flight_time +
                      norm_controller_time * weight_controller_time)

    return weighted_score

probability_increase = calculate_lottery_probability(user_times, max_times)
if probability_increase > 1.5:
    probability_increase = 1.5
'SKYline周年庆活动抽奖概率增加{round(probability_increase, 2)*2}%'