 
# O(nlogn) time solution, O(n) space

def longtIncSubseq(array):
    seq = [None for x in array]
    min_index_seq = [None for x in range(len(array) + 1)]
    cur_length = 0
    for i, num in enumerate(array):
        newLength = binSch(1, cur_length, min_index_seq, array, num)
        seq[i] = min_index_seq[newLength - 1]
        min_index_seq[newLength] = i
        cur_length = max(cur_length, newLength)
    return construct_Seq(array, seq, min_index_seq[cur_length])


def binSch(startIdx, endIdx, indices, array, num):
    if startIdx > endIdx:
        return startIdx
    middleIdx = (startIdx + endIdx) // 2
    if array[indices[middleIdx]] < num:
        startIdx = middleIdx + 1
    else:
        endIdx = middleIdx - 1
    return binSch(startIdx, endIdx, indices, array, num)


def construct_Seq(array, seq, currentIdx):
    final_sequence = []
    while currentIdx is not None:
        final_sequence.append(array[currentIdx])
        currentIdx = seq[currentIdx]
    return list(reversed(final_sequence))

longtIncSubseq([1, 5, -1, 0, 6, 2, 4])   
#,

[-1, 0, 2, 4]

