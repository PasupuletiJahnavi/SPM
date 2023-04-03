from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
def token(rollno,seconds):
    s=Serializer('P@supuleti1302',seconds)
    return s.dumps({'user':rollno}).decode('utf-8')
