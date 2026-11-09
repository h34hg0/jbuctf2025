def list2byte(arr):
    result = b''
    for i in range(len(arr)):
        result += bytes({arr[i]})
    return result

def byte2list(b):
    return [b[i] for i in range(len(b))]

from table import table1, table2

class Cipher():

    def enc_block(self, block):
        tmp = [0 for _ in range(16)]
        tmp[ 0] = table1[0][0][ 0][block[ 0]][0] ^ table1[1][0][ 1][block[ 5]][0] ^ table1[2][0][ 2][block[10]][0] ^ table1[3][0][ 3][block[15]][0]
        tmp[ 1] = table1[0][0][ 0][block[ 0]][1] ^ table1[1][0][ 1][block[ 5]][1] ^ table1[2][0][ 2][block[10]][1] ^ table1[3][0][ 3][block[15]][1]
        tmp[ 2] = table1[0][0][ 0][block[ 0]][2] ^ table1[1][0][ 1][block[ 5]][2] ^ table1[2][0][ 2][block[10]][2] ^ table1[3][0][ 3][block[15]][2]
        tmp[ 3] = table1[0][0][ 0][block[ 0]][3] ^ table1[1][0][ 1][block[ 5]][3] ^ table1[2][0][ 2][block[10]][3] ^ table1[3][0][ 3][block[15]][3]
        tmp[ 4] = table1[0][0][ 4][block[ 4]][0] ^ table1[1][0][ 5][block[ 9]][0] ^ table1[2][0][ 6][block[14]][0] ^ table1[3][0][ 7][block[ 3]][0]
        tmp[ 5] = table1[0][0][ 4][block[ 4]][1] ^ table1[1][0][ 5][block[ 9]][1] ^ table1[2][0][ 6][block[14]][1] ^ table1[3][0][ 7][block[ 3]][1]
        tmp[ 6] = table1[0][0][ 4][block[ 4]][2] ^ table1[1][0][ 5][block[ 9]][2] ^ table1[2][0][ 6][block[14]][2] ^ table1[3][0][ 7][block[ 3]][2]
        tmp[ 7] = table1[0][0][ 4][block[ 4]][3] ^ table1[1][0][ 5][block[ 9]][3] ^ table1[2][0][ 6][block[14]][3] ^ table1[3][0][ 7][block[ 3]][3]
        tmp[ 8] = table1[0][0][ 8][block[ 8]][0] ^ table1[1][0][ 9][block[13]][0] ^ table1[2][0][10][block[ 2]][0] ^ table1[3][0][11][block[ 7]][0]
        tmp[ 9] = table1[0][0][ 8][block[ 8]][1] ^ table1[1][0][ 9][block[13]][1] ^ table1[2][0][10][block[ 2]][1] ^ table1[3][0][11][block[ 7]][1]
        tmp[10] = table1[0][0][ 8][block[ 8]][2] ^ table1[1][0][ 9][block[13]][2] ^ table1[2][0][10][block[ 2]][2] ^ table1[3][0][11][block[ 7]][2]
        tmp[11] = table1[0][0][ 8][block[ 8]][3] ^ table1[1][0][ 9][block[13]][3] ^ table1[2][0][10][block[ 2]][3] ^ table1[3][0][11][block[ 7]][3]
        tmp[12] = table1[0][0][12][block[12]][0] ^ table1[1][0][13][block[ 1]][0] ^ table1[2][0][14][block[ 6]][0] ^ table1[3][0][15][block[11]][0]
        tmp[13] = table1[0][0][12][block[12]][1] ^ table1[1][0][13][block[ 1]][1] ^ table1[2][0][14][block[ 6]][1] ^ table1[3][0][15][block[11]][1]
        tmp[14] = table1[0][0][12][block[12]][2] ^ table1[1][0][13][block[ 1]][2] ^ table1[2][0][14][block[ 6]][2] ^ table1[3][0][15][block[11]][2]
        tmp[15] = table1[0][0][12][block[12]][3] ^ table1[1][0][13][block[ 1]][3] ^ table1[2][0][14][block[ 6]][3] ^ table1[3][0][15][block[11]][3]
        block = [tmp[i] for i in range(16)]

        tmp[ 0] = table1[0][1][ 0][block[ 0]][0] ^ table1[1][1][ 1][block[ 5]][0] ^ table1[2][1][ 2][block[10]][0] ^ table1[3][1][ 3][block[15]][0]
        tmp[ 1] = table1[0][1][ 0][block[ 0]][1] ^ table1[1][1][ 1][block[ 5]][1] ^ table1[2][1][ 2][block[10]][1] ^ table1[3][1][ 3][block[15]][1]
        tmp[ 2] = table1[0][1][ 0][block[ 0]][2] ^ table1[1][1][ 1][block[ 5]][2] ^ table1[2][1][ 2][block[10]][2] ^ table1[3][1][ 3][block[15]][2]
        tmp[ 3] = table1[0][1][ 0][block[ 0]][3] ^ table1[1][1][ 1][block[ 5]][3] ^ table1[2][1][ 2][block[10]][3] ^ table1[3][1][ 3][block[15]][3]
        tmp[ 4] = table1[0][1][ 4][block[ 4]][0] ^ table1[1][1][ 5][block[ 9]][0] ^ table1[2][1][ 6][block[14]][0] ^ table1[3][1][ 7][block[ 3]][0]
        tmp[ 5] = table1[0][1][ 4][block[ 4]][1] ^ table1[1][1][ 5][block[ 9]][1] ^ table1[2][1][ 6][block[14]][1] ^ table1[3][1][ 7][block[ 3]][1]
        tmp[ 6] = table1[0][1][ 4][block[ 4]][2] ^ table1[1][1][ 5][block[ 9]][2] ^ table1[2][1][ 6][block[14]][2] ^ table1[3][1][ 7][block[ 3]][2]
        tmp[ 7] = table1[0][1][ 4][block[ 4]][3] ^ table1[1][1][ 5][block[ 9]][3] ^ table1[2][1][ 6][block[14]][3] ^ table1[3][1][ 7][block[ 3]][3]
        tmp[ 8] = table1[0][1][ 8][block[ 8]][0] ^ table1[1][1][ 9][block[13]][0] ^ table1[2][1][10][block[ 2]][0] ^ table1[3][1][11][block[ 7]][0]
        tmp[ 9] = table1[0][1][ 8][block[ 8]][1] ^ table1[1][1][ 9][block[13]][1] ^ table1[2][1][10][block[ 2]][1] ^ table1[3][1][11][block[ 7]][1]
        tmp[10] = table1[0][1][ 8][block[ 8]][2] ^ table1[1][1][ 9][block[13]][2] ^ table1[2][1][10][block[ 2]][2] ^ table1[3][1][11][block[ 7]][2]
        tmp[11] = table1[0][1][ 8][block[ 8]][3] ^ table1[1][1][ 9][block[13]][3] ^ table1[2][1][10][block[ 2]][3] ^ table1[3][1][11][block[ 7]][3]
        tmp[12] = table1[0][1][12][block[12]][0] ^ table1[1][1][13][block[ 1]][0] ^ table1[2][1][14][block[ 6]][0] ^ table1[3][1][15][block[11]][0]
        tmp[13] = table1[0][1][12][block[12]][1] ^ table1[1][1][13][block[ 1]][1] ^ table1[2][1][14][block[ 6]][1] ^ table1[3][1][15][block[11]][1]
        tmp[14] = table1[0][1][12][block[12]][2] ^ table1[1][1][13][block[ 1]][2] ^ table1[2][1][14][block[ 6]][2] ^ table1[3][1][15][block[11]][2]
        tmp[15] = table1[0][1][12][block[12]][3] ^ table1[1][1][13][block[ 1]][3] ^ table1[2][1][14][block[ 6]][3] ^ table1[3][1][15][block[11]][3]
        block = [tmp[i] for i in range(16)]

        tmp[ 0] = table1[0][2][ 0][block[ 0]][0] ^ table1[1][2][ 1][block[ 5]][0] ^ table1[2][2][ 2][block[10]][0] ^ table1[3][2][ 3][block[15]][0]
        tmp[ 1] = table1[0][2][ 0][block[ 0]][1] ^ table1[1][2][ 1][block[ 5]][1] ^ table1[2][2][ 2][block[10]][1] ^ table1[3][2][ 3][block[15]][1]
        tmp[ 2] = table1[0][2][ 0][block[ 0]][2] ^ table1[1][2][ 1][block[ 5]][2] ^ table1[2][2][ 2][block[10]][2] ^ table1[3][2][ 3][block[15]][2]
        tmp[ 3] = table1[0][2][ 0][block[ 0]][3] ^ table1[1][2][ 1][block[ 5]][3] ^ table1[2][2][ 2][block[10]][3] ^ table1[3][2][ 3][block[15]][3]
        tmp[ 4] = table1[0][2][ 4][block[ 4]][0] ^ table1[1][2][ 5][block[ 9]][0] ^ table1[2][2][ 6][block[14]][0] ^ table1[3][2][ 7][block[ 3]][0]
        tmp[ 5] = table1[0][2][ 4][block[ 4]][1] ^ table1[1][2][ 5][block[ 9]][1] ^ table1[2][2][ 6][block[14]][1] ^ table1[3][2][ 7][block[ 3]][1]
        tmp[ 6] = table1[0][2][ 4][block[ 4]][2] ^ table1[1][2][ 5][block[ 9]][2] ^ table1[2][2][ 6][block[14]][2] ^ table1[3][2][ 7][block[ 3]][2]
        tmp[ 7] = table1[0][2][ 4][block[ 4]][3] ^ table1[1][2][ 5][block[ 9]][3] ^ table1[2][2][ 6][block[14]][3] ^ table1[3][2][ 7][block[ 3]][3]
        tmp[ 8] = table1[0][2][ 8][block[ 8]][0] ^ table1[1][2][ 9][block[13]][0] ^ table1[2][2][10][block[ 2]][0] ^ table1[3][2][11][block[ 7]][0]
        tmp[ 9] = table1[0][2][ 8][block[ 8]][1] ^ table1[1][2][ 9][block[13]][1] ^ table1[2][2][10][block[ 2]][1] ^ table1[3][2][11][block[ 7]][1]
        tmp[10] = table1[0][2][ 8][block[ 8]][2] ^ table1[1][2][ 9][block[13]][2] ^ table1[2][2][10][block[ 2]][2] ^ table1[3][2][11][block[ 7]][2]
        tmp[11] = table1[0][2][ 8][block[ 8]][3] ^ table1[1][2][ 9][block[13]][3] ^ table1[2][2][10][block[ 2]][3] ^ table1[3][2][11][block[ 7]][3]
        tmp[12] = table1[0][2][12][block[12]][0] ^ table1[1][2][13][block[ 1]][0] ^ table1[2][2][14][block[ 6]][0] ^ table1[3][2][15][block[11]][0]
        tmp[13] = table1[0][2][12][block[12]][1] ^ table1[1][2][13][block[ 1]][1] ^ table1[2][2][14][block[ 6]][1] ^ table1[3][2][15][block[11]][1]
        tmp[14] = table1[0][2][12][block[12]][2] ^ table1[1][2][13][block[ 1]][2] ^ table1[2][2][14][block[ 6]][2] ^ table1[3][2][15][block[11]][2]
        tmp[15] = table1[0][2][12][block[12]][3] ^ table1[1][2][13][block[ 1]][3] ^ table1[2][2][14][block[ 6]][3] ^ table1[3][2][15][block[11]][3]
        block = [tmp[i] for i in range(16)]
    
        tmp[ 0] = table1[0][3][ 0][block[ 0]][0] ^ table1[1][3][ 1][block[ 5]][0] ^ table1[2][3][ 2][block[10]][0] ^ table1[3][3][ 3][block[15]][0]
        tmp[ 1] = table1[0][3][ 0][block[ 0]][1] ^ table1[1][3][ 1][block[ 5]][1] ^ table1[2][3][ 2][block[10]][1] ^ table1[3][3][ 3][block[15]][1]
        tmp[ 2] = table1[0][3][ 0][block[ 0]][2] ^ table1[1][3][ 1][block[ 5]][2] ^ table1[2][3][ 2][block[10]][2] ^ table1[3][3][ 3][block[15]][2]
        tmp[ 3] = table1[0][3][ 0][block[ 0]][3] ^ table1[1][3][ 1][block[ 5]][3] ^ table1[2][3][ 2][block[10]][3] ^ table1[3][3][ 3][block[15]][3]
        tmp[ 4] = table1[0][3][ 4][block[ 4]][0] ^ table1[1][3][ 5][block[ 9]][0] ^ table1[2][3][ 6][block[14]][0] ^ table1[3][3][ 7][block[ 3]][0]
        tmp[ 5] = table1[0][3][ 4][block[ 4]][1] ^ table1[1][3][ 5][block[ 9]][1] ^ table1[2][3][ 6][block[14]][1] ^ table1[3][3][ 7][block[ 3]][1]
        tmp[ 6] = table1[0][3][ 4][block[ 4]][2] ^ table1[1][3][ 5][block[ 9]][2] ^ table1[2][3][ 6][block[14]][2] ^ table1[3][3][ 7][block[ 3]][2]
        tmp[ 7] = table1[0][3][ 4][block[ 4]][3] ^ table1[1][3][ 5][block[ 9]][3] ^ table1[2][3][ 6][block[14]][3] ^ table1[3][3][ 7][block[ 3]][3]
        tmp[ 8] = table1[0][3][ 8][block[ 8]][0] ^ table1[1][3][ 9][block[13]][0] ^ table1[2][3][10][block[ 2]][0] ^ table1[3][3][11][block[ 7]][0]
        tmp[ 9] = table1[0][3][ 8][block[ 8]][1] ^ table1[1][3][ 9][block[13]][1] ^ table1[2][3][10][block[ 2]][1] ^ table1[3][3][11][block[ 7]][1]
        tmp[10] = table1[0][3][ 8][block[ 8]][2] ^ table1[1][3][ 9][block[13]][2] ^ table1[2][3][10][block[ 2]][2] ^ table1[3][3][11][block[ 7]][2]
        tmp[11] = table1[0][3][ 8][block[ 8]][3] ^ table1[1][3][ 9][block[13]][3] ^ table1[2][3][10][block[ 2]][3] ^ table1[3][3][11][block[ 7]][3]
        tmp[12] = table1[0][3][12][block[12]][0] ^ table1[1][3][13][block[ 1]][0] ^ table1[2][3][14][block[ 6]][0] ^ table1[3][3][15][block[11]][0]
        tmp[13] = table1[0][3][12][block[12]][1] ^ table1[1][3][13][block[ 1]][1] ^ table1[2][3][14][block[ 6]][1] ^ table1[3][3][15][block[11]][1]
        tmp[14] = table1[0][3][12][block[12]][2] ^ table1[1][3][13][block[ 1]][2] ^ table1[2][3][14][block[ 6]][2] ^ table1[3][3][15][block[11]][2]
        tmp[15] = table1[0][3][12][block[12]][3] ^ table1[1][3][13][block[ 1]][3] ^ table1[2][3][14][block[ 6]][3] ^ table1[3][3][15][block[11]][3]
        block = [tmp[i] for i in range(16)]
    
        tmp[ 0] = table1[0][4][ 0][block[ 0]][0] ^ table1[1][4][ 1][block[ 5]][0] ^ table1[2][4][ 2][block[10]][0] ^ table1[3][4][ 3][block[15]][0]
        tmp[ 1] = table1[0][4][ 0][block[ 0]][1] ^ table1[1][4][ 1][block[ 5]][1] ^ table1[2][4][ 2][block[10]][1] ^ table1[3][4][ 3][block[15]][1]
        tmp[ 2] = table1[0][4][ 0][block[ 0]][2] ^ table1[1][4][ 1][block[ 5]][2] ^ table1[2][4][ 2][block[10]][2] ^ table1[3][4][ 3][block[15]][2]
        tmp[ 3] = table1[0][4][ 0][block[ 0]][3] ^ table1[1][4][ 1][block[ 5]][3] ^ table1[2][4][ 2][block[10]][3] ^ table1[3][4][ 3][block[15]][3]
        tmp[ 4] = table1[0][4][ 4][block[ 4]][0] ^ table1[1][4][ 5][block[ 9]][0] ^ table1[2][4][ 6][block[14]][0] ^ table1[3][4][ 7][block[ 3]][0]
        tmp[ 5] = table1[0][4][ 4][block[ 4]][1] ^ table1[1][4][ 5][block[ 9]][1] ^ table1[2][4][ 6][block[14]][1] ^ table1[3][4][ 7][block[ 3]][1]
        tmp[ 6] = table1[0][4][ 4][block[ 4]][2] ^ table1[1][4][ 5][block[ 9]][2] ^ table1[2][4][ 6][block[14]][2] ^ table1[3][4][ 7][block[ 3]][2]
        tmp[ 7] = table1[0][4][ 4][block[ 4]][3] ^ table1[1][4][ 5][block[ 9]][3] ^ table1[2][4][ 6][block[14]][3] ^ table1[3][4][ 7][block[ 3]][3]
        tmp[ 8] = table1[0][4][ 8][block[ 8]][0] ^ table1[1][4][ 9][block[13]][0] ^ table1[2][4][10][block[ 2]][0] ^ table1[3][4][11][block[ 7]][0]
        tmp[ 9] = table1[0][4][ 8][block[ 8]][1] ^ table1[1][4][ 9][block[13]][1] ^ table1[2][4][10][block[ 2]][1] ^ table1[3][4][11][block[ 7]][1]
        tmp[10] = table1[0][4][ 8][block[ 8]][2] ^ table1[1][4][ 9][block[13]][2] ^ table1[2][4][10][block[ 2]][2] ^ table1[3][4][11][block[ 7]][2]
        tmp[11] = table1[0][4][ 8][block[ 8]][3] ^ table1[1][4][ 9][block[13]][3] ^ table1[2][4][10][block[ 2]][3] ^ table1[3][4][11][block[ 7]][3]
        tmp[12] = table1[0][4][12][block[12]][0] ^ table1[1][4][13][block[ 1]][0] ^ table1[2][4][14][block[ 6]][0] ^ table1[3][4][15][block[11]][0]
        tmp[13] = table1[0][4][12][block[12]][1] ^ table1[1][4][13][block[ 1]][1] ^ table1[2][4][14][block[ 6]][1] ^ table1[3][4][15][block[11]][1]
        tmp[14] = table1[0][4][12][block[12]][2] ^ table1[1][4][13][block[ 1]][2] ^ table1[2][4][14][block[ 6]][2] ^ table1[3][4][15][block[11]][2]
        tmp[15] = table1[0][4][12][block[12]][3] ^ table1[1][4][13][block[ 1]][3] ^ table1[2][4][14][block[ 6]][3] ^ table1[3][4][15][block[11]][3]
        block = [tmp[i] for i in range(16)]
    
        tmp[ 0] = table1[0][5][ 0][block[ 0]][0] ^ table1[1][5][ 1][block[ 5]][0] ^ table1[2][5][ 2][block[10]][0] ^ table1[3][5][ 3][block[15]][0]
        tmp[ 1] = table1[0][5][ 0][block[ 0]][1] ^ table1[1][5][ 1][block[ 5]][1] ^ table1[2][5][ 2][block[10]][1] ^ table1[3][5][ 3][block[15]][1]
        tmp[ 2] = table1[0][5][ 0][block[ 0]][2] ^ table1[1][5][ 1][block[ 5]][2] ^ table1[2][5][ 2][block[10]][2] ^ table1[3][5][ 3][block[15]][2]
        tmp[ 3] = table1[0][5][ 0][block[ 0]][3] ^ table1[1][5][ 1][block[ 5]][3] ^ table1[2][5][ 2][block[10]][3] ^ table1[3][5][ 3][block[15]][3]
        tmp[ 4] = table1[0][5][ 4][block[ 4]][0] ^ table1[1][5][ 5][block[ 9]][0] ^ table1[2][5][ 6][block[14]][0] ^ table1[3][5][ 7][block[ 3]][0]
        tmp[ 5] = table1[0][5][ 4][block[ 4]][1] ^ table1[1][5][ 5][block[ 9]][1] ^ table1[2][5][ 6][block[14]][1] ^ table1[3][5][ 7][block[ 3]][1]
        tmp[ 6] = table1[0][5][ 4][block[ 4]][2] ^ table1[1][5][ 5][block[ 9]][2] ^ table1[2][5][ 6][block[14]][2] ^ table1[3][5][ 7][block[ 3]][2]
        tmp[ 7] = table1[0][5][ 4][block[ 4]][3] ^ table1[1][5][ 5][block[ 9]][3] ^ table1[2][5][ 6][block[14]][3] ^ table1[3][5][ 7][block[ 3]][3]
        tmp[ 8] = table1[0][5][ 8][block[ 8]][0] ^ table1[1][5][ 9][block[13]][0] ^ table1[2][5][10][block[ 2]][0] ^ table1[3][5][11][block[ 7]][0]
        tmp[ 9] = table1[0][5][ 8][block[ 8]][1] ^ table1[1][5][ 9][block[13]][1] ^ table1[2][5][10][block[ 2]][1] ^ table1[3][5][11][block[ 7]][1]
        tmp[10] = table1[0][5][ 8][block[ 8]][2] ^ table1[1][5][ 9][block[13]][2] ^ table1[2][5][10][block[ 2]][2] ^ table1[3][5][11][block[ 7]][2]
        tmp[11] = table1[0][5][ 8][block[ 8]][3] ^ table1[1][5][ 9][block[13]][3] ^ table1[2][5][10][block[ 2]][3] ^ table1[3][5][11][block[ 7]][3]
        tmp[12] = table1[0][5][12][block[12]][0] ^ table1[1][5][13][block[ 1]][0] ^ table1[2][5][14][block[ 6]][0] ^ table1[3][5][15][block[11]][0]
        tmp[13] = table1[0][5][12][block[12]][1] ^ table1[1][5][13][block[ 1]][1] ^ table1[2][5][14][block[ 6]][1] ^ table1[3][5][15][block[11]][1]
        tmp[14] = table1[0][5][12][block[12]][2] ^ table1[1][5][13][block[ 1]][2] ^ table1[2][5][14][block[ 6]][2] ^ table1[3][5][15][block[11]][2]
        tmp[15] = table1[0][5][12][block[12]][3] ^ table1[1][5][13][block[ 1]][3] ^ table1[2][5][14][block[ 6]][3] ^ table1[3][5][15][block[11]][3]
        block = [tmp[i] for i in range(16)]
    
        tmp[ 0] = table1[0][6][ 0][block[ 0]][0] ^ table1[1][6][ 1][block[ 5]][0] ^ table1[2][6][ 2][block[10]][0] ^ table1[3][6][ 3][block[15]][0]
        tmp[ 1] = table1[0][6][ 0][block[ 0]][1] ^ table1[1][6][ 1][block[ 5]][1] ^ table1[2][6][ 2][block[10]][1] ^ table1[3][6][ 3][block[15]][1]
        tmp[ 2] = table1[0][6][ 0][block[ 0]][2] ^ table1[1][6][ 1][block[ 5]][2] ^ table1[2][6][ 2][block[10]][2] ^ table1[3][6][ 3][block[15]][2]
        tmp[ 3] = table1[0][6][ 0][block[ 0]][3] ^ table1[1][6][ 1][block[ 5]][3] ^ table1[2][6][ 2][block[10]][3] ^ table1[3][6][ 3][block[15]][3]
        tmp[ 4] = table1[0][6][ 4][block[ 4]][0] ^ table1[1][6][ 5][block[ 9]][0] ^ table1[2][6][ 6][block[14]][0] ^ table1[3][6][ 7][block[ 3]][0]
        tmp[ 5] = table1[0][6][ 4][block[ 4]][1] ^ table1[1][6][ 5][block[ 9]][1] ^ table1[2][6][ 6][block[14]][1] ^ table1[3][6][ 7][block[ 3]][1]
        tmp[ 6] = table1[0][6][ 4][block[ 4]][2] ^ table1[1][6][ 5][block[ 9]][2] ^ table1[2][6][ 6][block[14]][2] ^ table1[3][6][ 7][block[ 3]][2]
        tmp[ 7] = table1[0][6][ 4][block[ 4]][3] ^ table1[1][6][ 5][block[ 9]][3] ^ table1[2][6][ 6][block[14]][3] ^ table1[3][6][ 7][block[ 3]][3]
        tmp[ 8] = table1[0][6][ 8][block[ 8]][0] ^ table1[1][6][ 9][block[13]][0] ^ table1[2][6][10][block[ 2]][0] ^ table1[3][6][11][block[ 7]][0]
        tmp[ 9] = table1[0][6][ 8][block[ 8]][1] ^ table1[1][6][ 9][block[13]][1] ^ table1[2][6][10][block[ 2]][1] ^ table1[3][6][11][block[ 7]][1]
        tmp[10] = table1[0][6][ 8][block[ 8]][2] ^ table1[1][6][ 9][block[13]][2] ^ table1[2][6][10][block[ 2]][2] ^ table1[3][6][11][block[ 7]][2]
        tmp[11] = table1[0][6][ 8][block[ 8]][3] ^ table1[1][6][ 9][block[13]][3] ^ table1[2][6][10][block[ 2]][3] ^ table1[3][6][11][block[ 7]][3]
        tmp[12] = table1[0][6][12][block[12]][0] ^ table1[1][6][13][block[ 1]][0] ^ table1[2][6][14][block[ 6]][0] ^ table1[3][6][15][block[11]][0]
        tmp[13] = table1[0][6][12][block[12]][1] ^ table1[1][6][13][block[ 1]][1] ^ table1[2][6][14][block[ 6]][1] ^ table1[3][6][15][block[11]][1]
        tmp[14] = table1[0][6][12][block[12]][2] ^ table1[1][6][13][block[ 1]][2] ^ table1[2][6][14][block[ 6]][2] ^ table1[3][6][15][block[11]][2]
        tmp[15] = table1[0][6][12][block[12]][3] ^ table1[1][6][13][block[ 1]][3] ^ table1[2][6][14][block[ 6]][3] ^ table1[3][6][15][block[11]][3]
        block = [tmp[i] for i in range(16)]
    
        tmp[ 0] = table1[0][7][ 0][block[ 0]][0] ^ table1[1][7][ 1][block[ 5]][0] ^ table1[2][7][ 2][block[10]][0] ^ table1[3][7][ 3][block[15]][0]
        tmp[ 1] = table1[0][7][ 0][block[ 0]][1] ^ table1[1][7][ 1][block[ 5]][1] ^ table1[2][7][ 2][block[10]][1] ^ table1[3][7][ 3][block[15]][1]
        tmp[ 2] = table1[0][7][ 0][block[ 0]][2] ^ table1[1][7][ 1][block[ 5]][2] ^ table1[2][7][ 2][block[10]][2] ^ table1[3][7][ 3][block[15]][2]
        tmp[ 3] = table1[0][7][ 0][block[ 0]][3] ^ table1[1][7][ 1][block[ 5]][3] ^ table1[2][7][ 2][block[10]][3] ^ table1[3][7][ 3][block[15]][3]
        tmp[ 4] = table1[0][7][ 4][block[ 4]][0] ^ table1[1][7][ 5][block[ 9]][0] ^ table1[2][7][ 6][block[14]][0] ^ table1[3][7][ 7][block[ 3]][0]
        tmp[ 5] = table1[0][7][ 4][block[ 4]][1] ^ table1[1][7][ 5][block[ 9]][1] ^ table1[2][7][ 6][block[14]][1] ^ table1[3][7][ 7][block[ 3]][1]
        tmp[ 6] = table1[0][7][ 4][block[ 4]][2] ^ table1[1][7][ 5][block[ 9]][2] ^ table1[2][7][ 6][block[14]][2] ^ table1[3][7][ 7][block[ 3]][2]
        tmp[ 7] = table1[0][7][ 4][block[ 4]][3] ^ table1[1][7][ 5][block[ 9]][3] ^ table1[2][7][ 6][block[14]][3] ^ table1[3][7][ 7][block[ 3]][3]
        tmp[ 8] = table1[0][7][ 8][block[ 8]][0] ^ table1[1][7][ 9][block[13]][0] ^ table1[2][7][10][block[ 2]][0] ^ table1[3][7][11][block[ 7]][0]
        tmp[ 9] = table1[0][7][ 8][block[ 8]][1] ^ table1[1][7][ 9][block[13]][1] ^ table1[2][7][10][block[ 2]][1] ^ table1[3][7][11][block[ 7]][1]
        tmp[10] = table1[0][7][ 8][block[ 8]][2] ^ table1[1][7][ 9][block[13]][2] ^ table1[2][7][10][block[ 2]][2] ^ table1[3][7][11][block[ 7]][2]
        tmp[11] = table1[0][7][ 8][block[ 8]][3] ^ table1[1][7][ 9][block[13]][3] ^ table1[2][7][10][block[ 2]][3] ^ table1[3][7][11][block[ 7]][3]
        tmp[12] = table1[0][7][12][block[12]][0] ^ table1[1][7][13][block[ 1]][0] ^ table1[2][7][14][block[ 6]][0] ^ table1[3][7][15][block[11]][0]
        tmp[13] = table1[0][7][12][block[12]][1] ^ table1[1][7][13][block[ 1]][1] ^ table1[2][7][14][block[ 6]][1] ^ table1[3][7][15][block[11]][1]
        tmp[14] = table1[0][7][12][block[12]][2] ^ table1[1][7][13][block[ 1]][2] ^ table1[2][7][14][block[ 6]][2] ^ table1[3][7][15][block[11]][2]
        tmp[15] = table1[0][7][12][block[12]][3] ^ table1[1][7][13][block[ 1]][3] ^ table1[2][7][14][block[ 6]][3] ^ table1[3][7][15][block[11]][3]
        block = [tmp[i] for i in range(16)]
    
        tmp[ 0] = table1[0][8][ 0][block[ 0]][0] ^ table1[1][8][ 1][block[ 5]][0] ^ table1[2][8][ 2][block[10]][0] ^ table1[3][8][ 3][block[15]][0]
        tmp[ 1] = table1[0][8][ 0][block[ 0]][1] ^ table1[1][8][ 1][block[ 5]][1] ^ table1[2][8][ 2][block[10]][1] ^ table1[3][8][ 3][block[15]][1]
        tmp[ 2] = table1[0][8][ 0][block[ 0]][2] ^ table1[1][8][ 1][block[ 5]][2] ^ table1[2][8][ 2][block[10]][2] ^ table1[3][8][ 3][block[15]][2]
        tmp[ 3] = table1[0][8][ 0][block[ 0]][3] ^ table1[1][8][ 1][block[ 5]][3] ^ table1[2][8][ 2][block[10]][3] ^ table1[3][8][ 3][block[15]][3]
        tmp[ 4] = table1[0][8][ 4][block[ 4]][0] ^ table1[1][8][ 5][block[ 9]][0] ^ table1[2][8][ 6][block[14]][0] ^ table1[3][8][ 7][block[ 3]][0]
        tmp[ 5] = table1[0][8][ 4][block[ 4]][1] ^ table1[1][8][ 5][block[ 9]][1] ^ table1[2][8][ 6][block[14]][1] ^ table1[3][8][ 7][block[ 3]][1]
        tmp[ 6] = table1[0][8][ 4][block[ 4]][2] ^ table1[1][8][ 5][block[ 9]][2] ^ table1[2][8][ 6][block[14]][2] ^ table1[3][8][ 7][block[ 3]][2]
        tmp[ 7] = table1[0][8][ 4][block[ 4]][3] ^ table1[1][8][ 5][block[ 9]][3] ^ table1[2][8][ 6][block[14]][3] ^ table1[3][8][ 7][block[ 3]][3]
        tmp[ 8] = table1[0][8][ 8][block[ 8]][0] ^ table1[1][8][ 9][block[13]][0] ^ table1[2][8][10][block[ 2]][0] ^ table1[3][8][11][block[ 7]][0]
        tmp[ 9] = table1[0][8][ 8][block[ 8]][1] ^ table1[1][8][ 9][block[13]][1] ^ table1[2][8][10][block[ 2]][1] ^ table1[3][8][11][block[ 7]][1]
        tmp[10] = table1[0][8][ 8][block[ 8]][2] ^ table1[1][8][ 9][block[13]][2] ^ table1[2][8][10][block[ 2]][2] ^ table1[3][8][11][block[ 7]][2]
        tmp[11] = table1[0][8][ 8][block[ 8]][3] ^ table1[1][8][ 9][block[13]][3] ^ table1[2][8][10][block[ 2]][3] ^ table1[3][8][11][block[ 7]][3]
        tmp[12] = table1[0][8][12][block[12]][0] ^ table1[1][8][13][block[ 1]][0] ^ table1[2][8][14][block[ 6]][0] ^ table1[3][8][15][block[11]][0]
        tmp[13] = table1[0][8][12][block[12]][1] ^ table1[1][8][13][block[ 1]][1] ^ table1[2][8][14][block[ 6]][1] ^ table1[3][8][15][block[11]][1]
        tmp[14] = table1[0][8][12][block[12]][2] ^ table1[1][8][13][block[ 1]][2] ^ table1[2][8][14][block[ 6]][2] ^ table1[3][8][15][block[11]][2]
        tmp[15] = table1[0][8][12][block[12]][3] ^ table1[1][8][13][block[ 1]][3] ^ table1[2][8][14][block[ 6]][3] ^ table1[3][8][15][block[11]][3]
        block = [tmp[i] for i in range(16)]

        tmp[ 0] = table2[ 0][block[ 0]]
        tmp[ 1] = table2[ 1][block[ 5]]  
        tmp[ 2] = table2[ 2][block[10]]
        tmp[ 3] = table2[ 3][block[15]]
        tmp[ 4] = table2[ 4][block[ 4]]
        tmp[ 5] = table2[ 5][block[ 9]]
        tmp[ 6] = table2[ 6][block[14]]
        tmp[ 7] = table2[ 7][block[ 3]]
        tmp[ 8] = table2[ 8][block[ 8]]
        tmp[ 9] = table2[ 9][block[13]]
        tmp[10] = table2[10][block[ 2]]
        tmp[11] = table2[11][block[ 7]]
        tmp[12] = table2[12][block[12]]
        tmp[13] = table2[13][block[ 1]]
        tmp[14] = table2[14][block[ 6]]
        tmp[15] = table2[15][block[11]]

        return tmp
    
    def encrypt(self, plaintext):
        blocks = [byte2list(plaintext[i:i+16]) for i in range(0, len(plaintext), 16)]

        result = b''
        for block in blocks:
            block = self.enc_block(block)
            result += list2byte(block)
        return result

if __name__ ==  '__main__':
    from Crypto.Random import get_random_bytes
    from Crypto.Cipher import AES 

    flag = open('./flag', 'r').read()
    flag = flag[len('scpCTF{'):-len('}')]
    key = bytes.fromhex(flag)

    cipher = AES.new(key, AES.MODE_ECB)
    myCipher = Cipher()

    for i in range(1000):
        p = get_random_bytes(16*8)
        c1 = cipher.encrypt(p)
        c2 = myCipher.encrypt(p)
        assert c1 == c2, 'Diff c1, c2'
    print(f'flag : scpCTF{{{key.hex()}}}')