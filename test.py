print ( '\n\n***********我的没有参数 的装饰器函数**************\n' )


def tips_pt ( func ):
    print ( 'tips_pt 不带参数的装饰器' )

    def tips ():
        print ( 'tips 不带参数的装饰器 准备执行' )
        func ()

    return tips


@tips_pt
def pt ():
    print ( '被调用函数已经执行' )


pt ()

print ( '\n\n***********被装饰函数带参数数 的装饰器**************\n' )


def tips ( func ):
    def inner ( a, b ):
        print ( 'start' )
        func ( a, b )

    # print ( 'stop  ')

    return inner


@tips
def add2 ( a, b ):
    print ( 'begin calc %s' % (a + b) )


# print(a+b)


add2 ( 3, 7 )


print ( '\n\n***********装饰器函数带参数数 的装饰器**************\n' )
def tips_add3 ( para ):
    print ( para )

    def tips ( func ):
        print ( 'start %s %s' % (para, func.__name__) )

        def inner ( a, b ):
            print ( 'start' )
            func ( a, b )

        # print ( 'stop  ')

        return inner

    return tips


@tips_add3 ( '装饰器函数带参数数' )
def add3 ( a, b ):
    print ( 'a+b  =  %s' % (a + b) )


# print(a+b)


add3 ( 3, 7 )
