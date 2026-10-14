frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"Python", "JavaScript", "SQL", "React"}

union_set = frontend_skills.union(backend_skills)

intersection_set = frontend_skills.intersection(backend_skills)

frontend_only = frontend_skills.difference(backend_skills)

symmetric_diff = frontend_skills.symmetric_difference(backend_skills)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Frontend-only:", frontend_only)
print("Symmetric Difference:", symmetric_diff)


# davaleba 2

student = { 
  "name": "Ana", 
  "age": 20, 
  "contacts": { 
      "email": "ana@example.com", 
      "phone": "599123456" 
    },
  "courses": {
      "python": {"score": 95, "passed": True},
      "web": {"score": 58, "passed": False} 
    } 
}


print(student["contacts"]["email"])
print(student["courses"]["python"]["score"])

student["courses"]["web"]["passed"] = True
student["courses"]["web"]["score"] = 65

del(student["contacts"]["phone"])

print(student)