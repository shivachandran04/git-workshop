# MDST Git & GitHub Workshop

This repo contains the materials for the MDST Git & GitHub workshop (first hosted Fall 2024). The `main/` branch contains the workshop instructions. The `project-*` branches contain the materials & spec for the specific assigned project.

## Instructions

1. One group member should fork this repository to their own GitHub account. Then, everybody should clone this forked repository to their local device. The member who forked the repository should invite everyone as contributors (workshop instructors included).
2. Depending on your team's assigned theme, switch branches to the correct branch with `git switch {branchname}`.
4. Switching to the branch will show all of your team's theme's starter code. Read the file called `SPEC.md`, and survey the starter code. `SPEC.md` contains more project-specific details.
5. The code assigns certain functions to "Person 1", "Person 2", ... Choose who "Person 1", "Person 2", ... refers to amongst yourselves, but DO NOT mix & match the numbers. i.e., functions that are assigned to "Person 1" must all be done by the same person. Who "Person 1" refers to in your specific group is up to group decision. 
6. Begin coding!

## Using Git & GitHub

As you complete the particular project your group is assigned to, follow this workflow:

```

Decide what functions everyone will implement.

Use GitHub issues to create an issue for each feature, and assign the issue to the relevant team members.

while (feature left to implement): 
  Decide what feature you will implement next.
  Create a new branch called `feat/{name_of_feature}`.
  Code.
  Push your changes.
  Open a pull request from your branch into the branch where your group intends to combine changes. This could be the `main` branch.
  Have other team members review this pull request, and approve it. Once approved, merge the pull request.
  Solve issues that arise along the way.
```

Refer to workshop materials, the workshop facilitators, ChatGPT, and Google (in that order) for help as issues arise.