        for first_divisor in list(all_divisors.keys()):

            # termination argument - otherwise the list will continue expanding
            if first_divisor > digits:
                break


            # now we begin the tricky part...
            for second_divisor in list(all_divisors.keys()):

                if second_divisor > digits:
                    break

                # termination argument - otherwise the list will continue expanding
                if first_divisor != second_divisor:
                    new_divisor = first_divisor + second_divisor
                    if digits % new_divisor != 0:

                        if new_divisor not in list(all_divisors.keys()):
                            all_divisors[new_divisor] = all_divisors[first_divisor] + all_divisors[second_divisor]
                    elif result != -1:
                        multiplier = digits // new_divisor
                        temp_result = ((all_divisors[first_divisor] * multiplier)  + (all_divisors[second_divisor] * multiplier))
                        temp_result = sorted(temp_result, reverse=True)
                        temp_result = "".join(temp_result)
                        if result < temp_result:
                            result = temp_result
                    else:
                        multiplier = digits // new_divisor
                        result = ((all_divisors[first_divisor] * multiplier) + (all_divisors[second_divisor] * multiplier))
                        result = sorted(result, reverse=True)
                        result = "".join(result)


    list_of_results.append(result)
    for item in list_of_results:
        print(item)
