# 提示信息
def comm ( chr ):
    ch = [chr]
    #ch2 = [0]

    def cmt ( st ):
        s = ''
        l = 0
        c = 0
        #ch2[0] += 1
        # print(type(ch2[0]))
        note = ch[0] + '   ' + st + '   ' + ch[0]
        #note = ch[0] + ' ' + str ( ch2[0] ) + '  ' + st + '   ' + ch[0]
        # print(len( note.encode( 'utf-8' ) ))
        x = 0
        while True:
            try:
                s = str ( hex ( ord ( note[x] ) ) )
                # print(s)

                l += len ( s ) - 2
                if len ( s ) == 6:
                    c += 1
                x += 1
            except IndexError:
                break
            finally:
                pass
        s = ''
        l = round ( l / 2 ) - round ( c / 3 ) - 1
        for x in range ( 0, l + 1 ):
            s += str ( ch[0] )[0]

        print ( s )
        print ( note )
        print ( s )

    return cmt


#
# pnt = comm( '#' )
# prt = comm('%')
# pnt( 'unicode' )
# prt('code格式')
#
comm ( '++' ) ( '格格式格式格式格式格式格式' )
comm ( '++' ) ( 'xxxxxx式格式格式格式格式格式' )
# +++++++++++++++++++++++++++++++
# ++   格格式格式格式格式格式格式   ++
# +++++++++++++++++++++++++++++++
