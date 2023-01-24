class Profile:
    _counter = 0
    def __init__(self, name, age, gender, looking_for_gender):
        self.id = Profile._counter
        Profile._counter += 1
        self.name = name
        self.age = age
        self.gender = gender
        self.looking_for_gender = looking_for_gender
        self.liked_profiles = []

class FreeProfile(Profile):
    def __init__(self, age, gender, looking_for_gender):
        super().__init__(self,age,gender,looking_for_gender)
        self.daily_likes = 1
        
    def like(self, profile):
        if profile == self:
            return "You can't like your own profile."
        elif profile.id in self.liked_profiles:
            return "You already liked this profile."
        elif self.daily_likes <= 0:
            return "You can't like more, you've reached your like limit."
        else:
            self.liked_profiles.append(profile.id)
            self.daily_likes -= 1
            return "Profile liked successfully."
            
    def send_message(self):
        return "Unable to send message, upgrade your profile to Pro."

class ProProfile(Profile):
    def __init__(self, name, age, gender, looking_for_gender):
        super().__init__(name, age, gender, looking_for_gender)
        self.daily_likes = 1000
        
    def like(self, profile):
        if profile == self:
            return "You can't like your own profile."
        elif profile.id in self.liked_profiles:
            return "You already liked this profile."
        elif self.daily_likes <= 0:
            return "You can't like more, you've reached your like limit."
        else:
            self.liked_profiles.append(profile.id)
            self.daily_likes -= 1
            return "Profile liked successfully."
            
    def send_message(self, profile, message):
        if profile.id not in self.liked_profiles:
            return "You can only send message to profile you have liked"
        else:
            print(f"Message is sent to profile #{profile.id}: {message}")

class DatingApp:
    def __init__(self, name):
        self.name = name
        self.profiles = []
        
    def register(self, *profiles):
        for profile in profiles:
            self.profiles.append(profile)
            
    def new_day(self):
        for profile in self.profiles:
            profile.daily_likes = 1000 if isinstance(profile, ProProfile) else 1
            
    def recommend_profiles(self, target):
        recommended_profiles = []
        for profile in self.profiles:
            if (profile.gender == target.looking_for_gender) and (profile.id not in target.liked_profiles) and (profile != target):
                recommended_profiles.append(profile.id)
                return recommended_profiles
            
    def who_liked_profile(self, profile):
        liked_by = []
        for p in self.profiles:
            if profile.id in p.liked_profiles:
                liked_by.append(p.id)
            return liked_by
        
    def advanced_recommend_profiles(self, target):
        recommended_profiles = []
        for profile in self.profiles:
            if (profile.gender == target.looking_for_gender) and (profile.id not in target.liked_profiles) and (profile != target):
                if profile.id in self.who_liked_profile(target):
                    recommended_profiles.insert(0, profile.id)
                else:
                    recommended_profiles.append(profile.id)
        return recommended_profiles

ibsnder = DatingApp('IBSnder')
john = ProProfile('John', 'male', 30, 'female') # should have profile id 1
jane = FreeProfile('female', 28, 'male') # should have profile id 2
kate = ProProfile('Kate', 'female', 34, 'female') # should have profile id 3
jack = FreeProfile('male', 23, 'male') # should have profile id 4
jill = ProProfile('Jill', 'female', 28, 'male') # should have profile id 5
bob = ProProfile('Bob', 'male', 42, 'female') # should have profile id 6
david = FreeProfile('male', 37, 'female') # should have profile id 7
ibsnder.register(john, jane, kate, jack, jill, bob, david)
print(john) # should print: John is a 30 year old male, looking for a female. (id: 1)
print(jane) # should print: 28 year old female, looking for a male. (id: 2)
john.likes(jane)
jane.likes(john) # should print: It's a match!
jane.likes(bob) # should print: You can't like more, you've reached your like limit.
john.likes(john) # should print: You can't like your own profile.
john.likes(kate)
jill.likes(john)
david.likes(jill)
print(ibsnder.recommend_profiles(jill)) # since Jill already liked John, it should print only: [6, 7]
print(ibsnder.advanced_recommend_profiles(jill)) # since David liked Jill, it should print only: [7, 6]
print(ibsnder.who_liked_profile(john)) # should print [2, 5]
ibsnder.new_day()
jane.likes(john) # should print: You already liked this profile.
jane.likes(bob) # no error, because Jane again has a free like
john.send_message(jane, 'hello') # should print: Message is sent to profile #2.
jane.send_message(john, 'hi') # Unable to send message, upgrade your profile to Pro

