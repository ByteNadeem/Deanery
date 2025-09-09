# Deanery Project Board Setup

This repository uses GitHub Project Boards with the **MoSCoW prioritization method** and **Kanban workflow** for project management.

## 🏷️ MoSCoW Priority Labels

The following labels are used to prioritize user stories and issues:

| Label | Color | Description |
|-------|-------|-------------|
| `MUST HAVE` | 🟢 Green (`#0E8A16`) | Critical functionality that is essential for the product |
| `SHOULD HAVE` | 🟡 Yellow (`#FBCA04`) | Important functionality that adds significant value |
| `COULD HAVE` | 🟠 Orange (`#F9D0C4`) | Nice-to-have functionality that would be beneficial |
| `WONT HAVE` | 🔴 Red (`#D73A49`) | Functionality that will not be implemented in this release |

## 📋 Project Board Structure (Kanban)

### Columns:
1. **📝 Backlog** - All user stories and issues waiting to be prioritized
2. **🔄 Ready** - Prioritized items ready to be worked on
3. **🏃 In Progress** - Items currently being worked on
4. **👀 In Review** - Completed work waiting for review/testing
5. **✅ Done** - Completed and reviewed items

### Workflow Rules:
- Items move from left to right through the columns
- Limit work in progress (WIP limits):
  - In Progress: Maximum 3 items per person
  - In Review: Maximum 5 items total
- All items must have a MoSCoW priority label
- MUST HAVE items take priority in all columns

## 📖 User Story Template

When creating user stories, use the provided template which includes:

### 1. Acceptance Criteria (Traditional Format)
```
AS A _____________(ROLE)
I WANT TO _________________(ACTION)
SO THAT ______________(FUNCTION)
```

### 2. Tasks Checklist
Default 3 numbered tasks with checkboxes:
```
1. [ ] Task 1 description
2. [ ] Task 2 description
3. [ ] Task 3 description
```

## 🚀 Getting Started

### Setting Up Labels
1. Go to the repository's **Issues** tab
2. Click on **Labels**
3. Import the labels from `.github/labels.yml` or create them manually:
   - **MUST HAVE**: Green color (`#0E8A16`)
   - **SHOULD HAVE**: Yellow color (`#FBCA04`)
   - **COULD HAVE**: Orange color (`#F9D0C4`)
   - **WONT HAVE**: Red color (`#D73A49`)

### Setting Up Project Board
1. Go to the repository's **Projects** tab
2. Click **New project**
3. Choose **Board** layout
4. Create columns as described above
5. Set up automation rules:
   - Auto-move items to "In Progress" when assigned
   - Auto-move to "Done" when issue is closed

### Creating User Stories
1. Go to **Issues** → **New issue**
2. Select **📖 User Story** template
3. Fill in all required sections
4. Add appropriate MoSCoW priority label
5. Assign to project board

## 📏 Best Practices

### For User Stories:
- Keep stories small and focused (completable in 1-2 sprints)
- Ensure acceptance criteria are testable
- Include all necessary context and mockups
- Break down large stories into smaller ones

### For Priority Management:
- Review and adjust priorities regularly
- Focus on MUST HAVE items first
- Don't overload MUST HAVE category
- Use WONT HAVE to explicitly defer features

### For Project Board:
- Update item status regularly
- Respect WIP limits
- Review board in daily standups
- Archive completed projects periodically

## 🔧 Automation

Consider setting up GitHub Actions for:
- Auto-labeling based on keywords
- Moving items between columns based on PR status
- Generating reports on priority distribution
- Notifying team of overdue items

## 📊 Metrics to Track

- **Velocity**: Items completed per sprint by priority
- **Priority Distribution**: Percentage of each MoSCoW category
- **Cycle Time**: Time from Ready to Done
- **Throughput**: Items completed per time period
- **Quality**: Items returned from Review to In Progress