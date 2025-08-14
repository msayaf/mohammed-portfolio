from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    """Home page view"""
    context = {
        'profile': {
            'name': 'Mohammed Saleem Sayaf',
            'title': 'M.Eng. in Structural Engineering',
            'bio': 'Passionate Structural Engineer with expertise in steel, concrete, and timber design. Currently pursuing M.Eng. in Structural Engineering at University of Alberta with experience in structural analysis, design, and project coordination.',
            'image': 'profile/mohammed.jpg',
        },
        'featured_projects': [],
        'skills': [],
    }
    return render(request, 'main/home.html', context)

def about(request):
    """About page view"""
    context = {
        'profile': {
            'name': 'Mohammed Saleem Sayaf',
            'title': 'M.Eng. in Structural Engineering',
            'bio': '''I am a dedicated Structural Engineer currently completing my Master of Engineering in Structural Engineering at the University of Alberta (2023-2025). With a strong foundation in Civil Engineering from India and practical experience in structural design and project coordination, I bring both theoretical knowledge and hands-on expertise to every project.
            
            My experience spans from structural analysis and design using industry-standard software to managing complex construction projects including PEB structures and reinforced concrete foundations. I have a particular interest in sustainable infrastructure systems and advanced structural analysis methods.
            
            I am passionate about applying engineering principles to create safe, efficient, and innovative structural solutions. My goal is to contribute to the advancement of structural engineering practices while ensuring compliance with Canadian building codes and standards.''',
            'education': [
                {
                    'degree': 'M.Eng. in Structural Engineering',
                    'school': 'University of Alberta, Edmonton',
                    'year': '2023-2025',
                    'courses': 'Steel Design (CSA-S16), Concrete Design (CSA-A23.3), Timber Structures (CSA 086:19), Advanced Structural Analysis, Dynamics, FEM'
                },
                {
                    'degree': 'B.E. in Civil Engineering',
                    'school': 'Dayananda Sagar College of Engineering, Bengaluru',
                    'year': '2018-2021',
                    'courses': 'Steel Structures, RCC Design, Construction Management, Prestressed Concrete, Structural Analysis'
                },
                {
                    'degree': 'Diploma in Civil Engineering',
                    'school': 'P A Polytechnic, Mangalore',
                    'year': '2015-2018',
                    'courses': 'Fundamental and practical studies in all civil engineering specializations'
                }
            ]
        },
        'skills_by_category': {
            'structural_software': [
                {'name': 'ETABS', 'proficiency': 85},
                {'name': 'SAP 2000', 'proficiency': 85},
                {'name': 'STAAD Pro', 'proficiency': 80},
                {'name': 'ABAQUS (FEA)', 'proficiency': 75},
            ],
            'design_tools': [
                {'name': 'AutoCAD', 'proficiency': 90},
                {'name': 'Revit', 'proficiency': 70},
                {'name': 'Bluebeam', 'proficiency': 75},
                {'name': 'Microsoft Excel', 'proficiency': 90},
            ],
            'engineering_codes': [
                {'name': 'CSA-S16 (Steel)', 'proficiency': 80},
                {'name': 'CSA-A23.3 (Concrete)', 'proficiency': 80},
                {'name': 'CSA 086:19 (Timber)', 'proficiency': 75},
                {'name': 'NBCC 2020', 'proficiency': 70},
            ],
            'soft_skills': [
                {'name': 'Project Coordination', 'proficiency': 85},
                {'name': 'Technical Communication', 'proficiency': 90},
                {'name': 'Team Collaboration', 'proficiency': 90},
                {'name': 'Problem Solving', 'proficiency': 85},
            ]
        },
        'experience': [
            {
                'position': 'Structural Design Intern',
                'company': 'Civilsoft Structural Consultants',
                'location': 'Bengaluru, India',
                'duration': 'Jan 2023 - Apr 2023',
                'responsibilities': [
                    'Structural analysis and design of RCC and steel structures using ETABS, STAAD Pro, SAP 2000',
                    'Developed Excel-based calculation templates for concrete member design',
                    'Created structural drawings for design validation and project estimation'
                ]
            },
            {
                'position': 'Project Coordinator / Field Engineer',
                'company': 'Karnataka Constructions',
                'location': 'Chikkamagaluru, India',
                'duration': 'Nov 2021 - May 2022',
                'responsibilities': [
                    'Managed construction of PEB industrial facility with reinforced concrete substructure',
                    'Supervised fabrication and erection of steel trusses, columns, and EOT crane',
                    'Performed quantity take-off using Microsoft Excel and Bluebeam',
                    'Collaborated with multidisciplinary teams for technical problem-solving'
                ]
            }
        ]
    }
    return render(request, 'main/about.html', context)

def projects(request):
    """Projects page view"""
    context = {
        'projects': [
            {
                'title': 'Analysis of Castellated Beam Using Abaqus',
                'description': 'Comprehensive finite element analysis comparing castellated beams with traditional I-beams, focusing on deflection and stress patterns. Demonstrated improved bending stiffness performance for longer spans.',
                'technologies': ['ABAQUS', 'Finite Element Analysis', 'Structural Analysis', 'Steel Design'],
                'github_url': '',
                'live_url': '',
                'image_class': 'bg-primary',
                'icon': 'fas fa-calculator',
                'category': 'Academic Research'
            },
            {
                'title': 'One-Storey Wood Framed Office Building Design',
                'description': 'Complete structural design of timber office building in Nelson, BC, including load calculations, gravity and lateral load resisting systems following CSA 086:19 and NBCC 2020.',
                'technologies': ['CSA 086:19', 'NBCC 2020', 'Timber Design', 'SAP 2000', 'AutoCAD'],
                'github_url': '',
                'live_url': '',
                'image_class': 'bg-success',
                'icon': 'fas fa-building',
                'category': 'Design Project'
            },
            {
                'title': 'Solar Tree Project using Timber',
                'description': 'Sustainable timber solar PV tree design combining clean energy generation with eco-friendly construction. Analyzed and modeled using SAP 2000 and Revit with innovative connection design.',
                'technologies': ['SAP 2000', 'Revit', 'Sustainable Design', 'Timber Engineering'],
                'github_url': '',
                'live_url': '',
                'image_class': 'bg-warning',
                'icon': 'fas fa-solar-panel',
                'category': 'Innovation Project'
            },
            {
                'title': 'Timber Moment Resisting Connections Evaluation',
                'description': 'Capstone project evaluating performance of various timber connections including slotted-in steel plate bolted, glued-in rod, and inclined screwed connections for improved ductility.',
                'technologies': ['Connection Design', 'Timber Engineering', 'Performance Analysis', 'Research'],
                'github_url': '',
                'live_url': '',
                'image_class': 'bg-info',
                'icon': 'fas fa-hammer',
                'category': 'Capstone Project'
            },
        ]
    }
    return render(request, 'main/projects.html', context)

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # For now, just show success message
        messages.success(request, f'Thank you {name}! Your message has been received. I will get back to you soon.')
        return redirect('contact')
    
    context = {
        'profile': {
            'email': 'sayafsaleem@gmail.com',
            'phone': '(587) 341-3258',
            'location': 'Edmonton, AB, Canada',
            'linkedin': 'https://linkedin.com/in/mohammed-sayaf',  # Update with your actual LinkedIn
            'github': 'https://github.com/mohammed-sayaf',  # Update with your actual GitHub
            'twitter': '',  # Add if you have Twitter
        },
        'certifications': [
            'Engineer-in-training with APEGA (Application in progress)',
            'Alberta Class 5 driver\'s license',
            'Construction Safety Training System (CSTS 2020)'
        ]
    }
    return render(request, 'main/contact.html', context)