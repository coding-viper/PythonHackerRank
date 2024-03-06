if __name__ == '__main__':
    limit=int(input())
    a=[[input(),float(input())][::-1] for _ in range(limit)]
    second=sorted({i for i,j in a })[1]
    print('\n'.join(sorted([j for i,j in a if i==second])))
    
# github:@coding-viper
