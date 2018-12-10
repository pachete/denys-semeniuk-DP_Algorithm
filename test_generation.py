from random import sample, random, randint


def convert_index(num, agent_number):
    agent_lst = [str(x) for x in range(agent_number, 0, -1)]
    # agent_lst = [x for x in range(agent_number, 0, -1)]

    binary_string = str(bin(num)[2:])
    binary_string = (agent_number - len(binary_string)) * "0" + binary_string
    result = str()
    # result = list()

    for i in range(len(binary_string) - 1, -1, -1):
        if binary_string[i] == '1':
            result += agent_lst[i]
            # result.append(agent_lst[i])

    return result


def generate_test(agent_number, low_limit, high_limit):
    result = dict()
    agent_lst = [x for x in sample(range(low_limit, high_limit), agent_number)]

    for coalition_index in range(1, 2 ** agent_number):
        random_sum = 0
        coalition_string = convert_index(coalition_index, agent_number)

        for agent in coalition_string:
            random_sum += agent_lst[int(agent) - 1]

        if len(coalition_string) > 1:
            random_add = randint(low_limit, (low_limit + high_limit) / 2)
            if random() < 0.5:
                random_sum += random_add
            else:
                random_sum -= random_add

        result[coalition_string] = random_sum
        # result[tuple(coalition_string)] = random_sum

    return agent_lst, result


if __name__ == "__main__":
    agents = 15
    low = 40
    high = 200

    agents_list, test_data = generate_test(agents, low, high)

    print(agents_list)
    print(test_data)
