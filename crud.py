class JobPortal:
    def __init__(self):
        self.jobs=[]
    def home(self):
        n=int(input("Enter number of jobs:"))
        while(1):
            print("Press 1:To create a Job")
            print("Press 2:To update a Job")
            print("Press 3:To delete the Jobs")
            print("Press 4:To display the Jobs ")
            print("Press 5:Exit")
            num=int(input("Enter the value of num:"))
            if num==1:
                print("Creating a Job")
                self.create(self.jobs)
            elif num==2:
                print("adding new skills to the existing jobs")
                self.update(self.jobs)
            elif num==3:
                print("Deleting the Jobs")
                self.delete(self.jobs)
            elif num==4:
                self.display(self.jobs)
            else:
                exit(0)
    def create(self,jobs):
        found=0
        new=str(input("Enter a new Job:"))
        for i in range(0,len(jobs)):
            if jobs[i] == new:
                found=1
                print("This job already exists")
                break
        if(found==0):
            jobs.append(new)
    def update(self,jobs):
        mod=str(input("Enter the Job you want to modify:"))
        modv=str(input("Enter the Modified Job:"))
        for i in range(0,len(jobs)):
            if jobs[i] == mod:
                jobs[i]=modv
            else:
                print("This job isn't exists")
    def delete(self,jobs):
        n=input("Enter the job to be deleted:")
        if n in jobs:
            jobs.remove(n)
    def display(self,jobs):
        for i in range(0,len(jobs)):
            print(jobs[i],end=" ")
        print()
obj=JobPortal()
obj.home()
