import csv


def test_1(data):
    for i in range(len(data)):
        try:
            assert len(data[i]) == 3, "found more than 3 columns at"
            a,b,c = data[i]
            if type(a) != str or type(b) != str or type(c) != str:
                print("found non string at", i)
        except Exception as e:
            print("crashed at", i)
            print("reason", e)

def test_2(data):
    for i in range(len(data)):
        try:
            a = int(data[i][1])
            print("did not fail int conv at", i)
        except:
            pass
        try:
            a = float(data[i][1])
            print("did not fail float conv at", i)
        except:
            pass
with open("topic.csv") as t:
    r = csv.reader(t)
    data = list(r)
    print("testing wether in right format")
    test_1(data)
    print("testing conversion")
    test_2(data)
