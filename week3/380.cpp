class RandomizedSet {
    vector<int> v;
    unordered_map<int,int> randomSet;
public:
   
    RandomizedSet() {
    }

    bool search(int val){
         if(randomSet.find(val)!=randomSet.end())
            return true;
         return false;
    }
    
    bool insert(int val) {

        if(search(val))
            return false;

        v.push_back(val);
        randomSet[val] = v.size()-1;
        return true;
    }
    
    bool remove(int val) {
        if(!search(val))
            return false;
       
        auto it = randomSet.find(val);
        v[it->second] = v.back();
        v.pop_back();
        randomSet[v[it->second]] = it->second;
        randomSet.erase(val);
        return true;
    }
    int getRandom() {
        return v[rand()%v.size()];
    }
};

