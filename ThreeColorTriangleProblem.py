import random
class ThreeC_Tri_Problem:
    
    def __init__ (self):
        self.colors = []
        self.check = 0
    
    def play(self, n):
        self.colors = []
        for i in range(n):
            self.colors.append([])
            self.colors[i] = [0]*(n-i)
        for j in range(n):
            self.colors[0][j] = random.randint(0,2)
        for k in range(1,n):
            for l in range (n-k):
                if self.colors[k-1][l] == self.colors[k-1][l+1]:
                    self.colors[k][l] = self.colors[k-1][l]
                else:
                    self.colors[k][l] = 3 - self.colors[k-1][l] - self.colors[k-1][l+1]
        return None
    def indicate1(self,n):
        self.play(n)
        for m in range(n):
            print "line"+str(m+1)+":"+str(self.colors[m])
            
    def check1(self, n, times):
        count = 0
        for i in range(times):
            self.play(n)
            if self.colors[0][0] == self.colors[0][n-1]:
                forecast = self.colors[0][0]
            else:
                forecast = 3-self.colors[0][0]-self.colors[0][n-1]
            
            if forecast == self.colors[n-1][0]:
                count += 1
        if count == times:
            self.check = 1
        else:
            self.check = 0
            
    def check_all(self, n, times):
        print "Following numbers is fit for the forecast: "
        for i in range(1,n):
            self.check1(i+1, times)
            if self.check == 1:
                print i+1


F = ThreeC_Tri_Problem()
F.check_all(50,100)