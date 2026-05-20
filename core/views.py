from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage, NewsletterSubscriber

SERVICES_DATA = {
    'financial-planning-budgeting': {
        'icon': 'fas fa-clipboard-list',
        'color': '#e94560',
        'gradient': 'linear-gradient(135deg, #e94560, #c73750)',
        'title': 'Financial Planning & Budgeting',
        'tagline': 'Your Financial GPS for Smarter Growth',
        'short_desc': 'Strategic financial roadmaps and budget frameworks for growth.',
        'desc': 'We create strategic financial roadmaps and budget frameworks designed to fuel your business growth. Our team works closely with you to understand your unique business goals, industry dynamics, and market conditions to build actionable financial plans that drive measurable results. Whether you are a startup looking to allocate your first round of funding or an established business aiming to scale operations, our tailored budgeting approach ensures every rupee is strategically deployed for maximum impact.',
        'highlights': [
            {'number': '200+', 'label': 'Budgets Prepared'},
            {'number': '35%', 'label': 'Avg. Cost Savings'},
            {'number': '98%', 'label': 'Client Retention'},
            {'number': '10+', 'label': 'Years Experience'},
        ],
        'features': [
            'Annual & quarterly budget preparation',
            'Revenue & expense forecasting',
            'Capital allocation strategy',
            'Scenario-based financial modeling',
            'Budget vs Actual variance analysis',
            'Strategic investment planning',
            'Cost reduction & optimization planning',
            'Departmental budget allocation',
            'Long-term financial goal setting',
            'Break-even & profitability analysis',
        ],
        'benefits': [
            {'icon': 'fas fa-chart-line', 'title': 'Data-Driven Decisions', 'text': 'Make every financial decision backed by real numbers and projections, not guesswork.'},
            {'icon': 'fas fa-piggy-bank', 'title': 'Maximize Savings', 'text': 'Identify cost leaks and redirect funds to high-impact areas that drive growth.'},
            {'icon': 'fas fa-shield-alt', 'title': 'Risk Protection', 'text': 'Scenario planning prepares you for market shifts, downturns, and unexpected expenses.'},
            {'icon': 'fas fa-rocket', 'title': 'Accelerate Growth', 'text': 'Strategically allocate capital to opportunities that generate the highest returns.'},
        ],
        'why_it_matters': 'Without a solid financial plan, businesses often face cash shortages, overspending, and missed growth opportunities. A well-structured budget acts as your financial GPS — guiding every decision, preventing costly mistakes, and keeping your business on track towards its goals.',
        'ideal_for': [
            {'icon': 'fas fa-seedling', 'text': 'Startups allocating first round funding'},
            {'icon': 'fas fa-building', 'text': 'SMEs looking to scale operations'},
            {'icon': 'fas fa-expand-arrows-alt', 'text': 'Companies planning expansion'},
            {'icon': 'fas fa-sync-alt', 'text': 'Businesses undergoing restructuring'},
        ],
        'process': [
            {'step': 'Discovery', 'text': 'We analyze your current financial position, business model, and growth aspirations.'},
            {'step': 'Framework Design', 'text': 'We create a customized budget structure aligned with your business departments and goals.'},
            {'step': 'Forecasting', 'text': 'Revenue projections, expense forecasting, and scenario modeling for different outcomes.'},
            {'step': 'Implementation', 'text': 'We set up tracking systems and reporting mechanisms for real-time budget monitoring.'},
            {'step': 'Review & Optimize', 'text': 'Monthly variance analysis and quarterly plan adjustments to keep you on track.'},
        ],
        'faqs': [
            {'q': 'How long does it take to prepare a financial plan?', 'a': 'Typically 2-3 weeks for a comprehensive plan, depending on business complexity and data availability.'},
            {'q': 'Do you work with startups that have no financial history?', 'a': 'Absolutely! We specialize in building financial frameworks from scratch for startups using industry benchmarks and market analysis.'},
            {'q': 'How often should a budget be reviewed?', 'a': 'We recommend monthly variance analysis and quarterly full reviews to keep your plan aligned with changing business conditions.'},
            {'q': 'What tools do you use for financial planning?', 'a': 'We use a combination of advanced Excel models, Tally integration, and custom dashboard tools tailored to your business.'},
        ],
    },
    'liquidity-management': {
        'icon': 'fas fa-tint',
        'color': '#3b82f6',
        'gradient': 'linear-gradient(135deg, #3b82f6, #2563eb)',
        'title': 'Liquidity Management',
        'tagline': 'Keep Your Cash Flowing, Always',
        'short_desc': 'Ensure healthy cash reserves and optimal fund utilization.',
        'desc': 'Ensure healthy cash reserves and optimal fund utilization with our expert liquidity management services. We help you maintain the perfect balance between having enough cash to meet obligations and investing surplus funds for maximum returns. Our proactive approach identifies potential cash flow gaps weeks in advance, giving you ample time to take corrective action. We analyze your entire cash conversion cycle — from receivables to payables — and design strategies that keep your business financially agile.',
        'highlights': [
            {'number': '150+', 'label': 'Cash Plans Designed'},
            {'number': '40%', 'label': 'Working Capital Improved'},
            {'number': '3x', 'label': 'Faster Cash Recovery'},
            {'number': '24/7', 'label': 'Cash Monitoring'},
        ],
        'features': [
            'Cash flow forecasting & monitoring',
            'Working capital optimization',
            'Fund allocation & reserve planning',
            'Short-term investment strategies',
            'Debt management & refinancing advice',
            'Emergency fund planning',
            'Cash conversion cycle analysis',
            'Bank relationship management',
            'Credit line optimization',
            'Seasonal cash flow planning',
        ],
        'benefits': [
            {'icon': 'fas fa-tachometer-alt', 'title': 'Real-Time Visibility', 'text': 'Know your exact cash position at any moment — no surprises, no last-minute scrambles.'},
            {'icon': 'fas fa-hand-holding-usd', 'title': 'Optimal Fund Use', 'text': 'Never let idle cash sit unused — every rupee works for your business growth.'},
            {'icon': 'fas fa-exclamation-triangle', 'title': 'Early Warning System', 'text': 'Spot cash flow gaps weeks before they happen and take corrective action in time.'},
            {'icon': 'fas fa-balance-scale', 'title': 'Perfect Balance', 'text': 'Maintain ideal balance between safety reserves and growth investments.'},
        ],
        'why_it_matters': 'Cash is the lifeblood of any business. Even profitable companies can fail if they run out of cash. Effective liquidity management ensures you can always pay suppliers on time, meet payroll, seize unexpected opportunities, and weather economic downturns without panic.',
        'ideal_for': [
            {'icon': 'fas fa-calendar-alt', 'text': 'Businesses with seasonal revenue'},
            {'icon': 'fas fa-project-diagram', 'text': 'Companies managing multiple projects'},
            {'icon': 'fas fa-exchange-alt', 'text': 'Complex payment cycle organizations'},
            {'icon': 'fas fa-industry', 'text': 'Manufacturing & trading businesses'},
        ],
        'process': [
            {'step': 'Cash Flow Audit', 'text': 'We map your entire cash inflow and outflow cycle to identify patterns and gaps.'},
            {'step': 'Working Capital Analysis', 'text': 'Deep dive into receivables, payables, and inventory to find optimization opportunities.'},
            {'step': 'Strategy Design', 'text': 'Create a liquidity strategy balancing safety reserves with growth investments.'},
            {'step': 'System Setup', 'text': 'Implement cash flow tracking dashboards and early warning alerts.'},
            {'step': 'Ongoing Monitoring', 'text': 'Weekly cash position reviews and monthly strategy refinements.'},
        ],
        'faqs': [
            {'q': 'How quickly can you improve our cash flow?', 'a': 'Most businesses see noticeable improvement within 4-6 weeks as we optimize receivables collection and payment scheduling.'},
            {'q': 'Do you help with bank negotiations?', 'a': 'Yes, we assist with credit line negotiations, overdraft facility setup, and building strong bank relationships for better terms.'},
            {'q': 'What if our business has highly unpredictable cash flows?', 'a': 'We specialize in designing flexible strategies with buffer reserves and contingency plans for volatile cash flow businesses.'},
            {'q': 'Can you integrate with our existing accounting software?', 'a': 'Absolutely! We work with Tally, Zoho Books, QuickBooks, and other popular accounting platforms.'},
        ],
    },
    'kra-kpi-tracking': {
        'icon': 'fas fa-bullseye',
        'color': '#10b981',
        'gradient': 'linear-gradient(135deg, #10b981, #059669)',
        'title': 'KRA-KPI Tracking',
        'tagline': 'Measure What Matters, Grow What Counts',
        'short_desc': 'Track key performance indicators for business and employee performance.',
        'desc': 'Track key performance indicators for business and employee performance with precision and clarity. Our customized KPI frameworks ensure every team member is aligned with your business objectives, creating a culture of accountability and continuous improvement. We don\'t just set metrics — we design complete performance ecosystems that connect individual goals to departmental targets and ultimately to your company\'s vision. Regular performance reviews powered by data-driven insights help you identify top performers, address underperformance early, and make informed decisions about promotions, training, and resource allocation.',
        'highlights': [
            {'number': '500+', 'label': 'KPIs Designed'},
            {'number': '45%', 'label': 'Productivity Boost'},
            {'number': '100+', 'label': 'Teams Transformed'},
            {'number': '12+', 'label': 'Industries Served'},
        ],
        'features': [
            'Custom KPI framework design',
            'Department-wise KRA setting',
            'Monthly performance scorecards',
            'Employee productivity metrics',
            'Goal alignment with business objectives',
            'Automated tracking dashboards',
            'Quarterly performance review setup',
            'Incentive & bonus structure design',
            'Team & individual benchmarking',
            'Performance improvement action plans',
        ],
        'benefits': [
            {'icon': 'fas fa-bullseye', 'title': 'Clear Direction', 'text': 'Every team member knows exactly what\'s expected and how their work impacts the company.'},
            {'icon': 'fas fa-trophy', 'title': 'Reward Top Performers', 'text': 'Data-driven insights make it easy to identify and reward your best contributors.'},
            {'icon': 'fas fa-users-cog', 'title': 'Team Alignment', 'text': 'Connect individual goals to departmental targets and company vision seamlessly.'},
            {'icon': 'fas fa-chart-bar', 'title': 'Measurable Progress', 'text': 'Track real progress with scorecards that replace guesswork with hard numbers.'},
        ],
        'why_it_matters': 'What gets measured gets managed. Without clear KRAs and KPIs, employees work without direction, managers make decisions based on gut feeling, and the business loses focus. A structured tracking system brings transparency, motivation, and measurable progress across the organization.',
        'ideal_for': [
            {'icon': 'fas fa-users', 'text': 'Companies with 10+ employees'},
            {'icon': 'fas fa-chart-line', 'text': 'Businesses scaling their teams'},
            {'icon': 'fas fa-medal', 'text': 'Performance-driven organizations'},
            {'icon': 'fas fa-cogs', 'text': 'Companies building HR systems'},
        ],
        'process': [
            {'step': 'Goal Mapping', 'text': 'We align your company vision with departmental and individual goals.'},
            {'step': 'KRA-KPI Design', 'text': 'Define measurable KRAs and KPIs for each role and department.'},
            {'step': 'Scorecard Creation', 'text': 'Build performance scorecards with clear rating criteria and benchmarks.'},
            {'step': 'Dashboard Setup', 'text': 'Implement automated tracking tools for real-time performance visibility.'},
            {'step': 'Review Cycle', 'text': 'Establish monthly reviews and quarterly performance assessments.'},
        ],
        'faqs': [
            {'q': 'How many KPIs should each employee have?', 'a': 'We recommend 5-7 KPIs per role — enough to cover key responsibilities without overwhelming the tracking process.'},
            {'q': 'Can this work for small teams of 5-10 people?', 'a': 'Yes! We design lightweight frameworks for small teams that are easy to manage and scale as you grow.'},
            {'q': 'How do you handle subjective roles like creative teams?', 'a': 'We blend quantitative metrics with qualitative assessments, using peer reviews and project-based evaluations.'},
            {'q': 'Do you provide the tracking software?', 'a': 'We help you set up dashboards using tools you already use (Excel, Google Sheets) or recommend specialized platforms.'},
        ],
    },
    'internal-control-system': {
        'icon': 'fas fa-lock',
        'color': '#f59e0b',
        'gradient': 'linear-gradient(135deg, #f59e0b, #d97706)',
        'title': 'Internal Control System',
        'tagline': 'Protect Your Business from the Inside Out',
        'short_desc': 'Set up robust internal controls to prevent fraud and ensure compliance.',
        'desc': 'Set up robust internal controls to prevent fraud, minimize errors, and ensure regulatory compliance. We design comprehensive control frameworks that protect your business assets while maintaining operational efficiency. Our approach goes beyond simple checklists — we analyze your entire business process flow, identify vulnerability points, and implement layered controls that catch issues before they become problems. From authorization hierarchies to automated reconciliation processes, we build systems that give you peace of mind while allowing your business to operate smoothly.',
        'highlights': [
            {'number': '100+', 'label': 'Controls Implemented'},
            {'number': '99%', 'label': 'Fraud Prevention Rate'},
            {'number': '50+', 'label': 'Audits Supported'},
            {'number': '0', 'label': 'Compliance Failures'},
        ],
        'features': [
            'Process audit & risk assessment',
            'Fraud prevention mechanisms',
            'Authorization & approval workflows',
            'Compliance framework setup',
            'Segregation of duties implementation',
            'Periodic internal audit reviews',
            'Inventory control procedures',
            'Financial reporting controls',
            'IT access & data security controls',
            'Whistleblower policy & ethics framework',
        ],
        'benefits': [
            {'icon': 'fas fa-lock', 'title': 'Fraud Prevention', 'text': 'Multi-layered controls that catch irregularities before they become costly problems.'},
            {'icon': 'fas fa-clipboard-check', 'title': 'Audit Ready', 'text': 'Stay always prepared for statutory audits with documented processes and clear trails.'},
            {'icon': 'fas fa-handshake', 'title': 'Stakeholder Trust', 'text': 'Build confidence among investors, partners, and regulators with transparent operations.'},
            {'icon': 'fas fa-cog', 'title': 'Smooth Operations', 'text': 'Controls that protect without slowing down — efficiency and security in perfect balance.'},
        ],
        'why_it_matters': 'Internal fraud and errors cost Indian businesses crores every year. A strong internal control system is not just about preventing theft — it\'s about building a trustworthy organization where processes are reliable, financial reports are accurate, and stakeholders have confidence in your operations.',
        'ideal_for': [
            {'icon': 'fas fa-chart-line', 'text': 'Growing businesses scaling operations'},
            {'icon': 'fas fa-file-alt', 'text': 'Companies preparing for audit'},
            {'icon': 'fas fa-exchange-alt', 'text': 'High transaction volume organizations'},
            {'icon': 'fas fa-map-marker-alt', 'text': 'Multi-location businesses'},
        ],
        'process': [
            {'step': 'Risk Assessment', 'text': 'Identify high-risk areas across all departments and processes.'},
            {'step': 'Control Design', 'text': 'Design preventive and detective controls tailored to your business.'},
            {'step': 'Policy Documentation', 'text': 'Create clear SOPs, authorization matrices, and compliance checklists.'},
            {'step': 'Implementation', 'text': 'Roll out controls with employee training and change management.'},
            {'step': 'Audit & Review', 'text': 'Periodic testing and updates to ensure controls remain effective.'},
        ],
        'faqs': [
            {'q': 'Will internal controls slow down our operations?', 'a': 'No! We design controls that are efficient and streamlined — they protect your business without creating bottlenecks.'},
            {'q': 'How do you handle resistance from employees?', 'a': 'We include change management and training as part of implementation, helping employees understand the "why" behind each control.'},
            {'q': 'Is this only for large companies?', 'a': 'Not at all. Even businesses with 5-10 employees benefit from basic controls — we scale the framework to match your size.'},
            {'q': 'How often should controls be reviewed?', 'a': 'We recommend quarterly reviews for high-risk areas and annual comprehensive audits for the entire control framework.'},
        ],
    },
    'finance-dashboards': {
        'icon': 'fas fa-laptop',
        'color': '#8b5cf6',
        'gradient': 'linear-gradient(135deg, #8b5cf6, #7c3aed)',
        'title': 'Finance Dashboards',
        'tagline': 'See Your Numbers, Seize the Moment',
        'short_desc': 'Real-time visual dashboards for instant financial insights.',
        'desc': 'Real-time visual dashboards for instant financial insights that empower faster, smarter decisions. Get a bird\'s eye view of your company\'s financial health with our custom-built dashboard solutions. We transform your raw financial data into interactive, easy-to-understand visual reports that update in real-time. No more waiting for month-end reports or manually compiling spreadsheets — see your revenue, expenses, margins, and cash position at a glance. Our dashboards are designed for both finance teams and business owners, with drill-down capabilities that let you go from high-level summaries to transaction-level details in just a few clicks.',
        'highlights': [
            {'number': '80+', 'label': 'Dashboards Built'},
            {'number': '5min', 'label': 'Setup to Insight'},
            {'number': '100%', 'label': 'Real-Time Data'},
            {'number': '50+', 'label': 'Metric Templates'},
        ],
        'features': [
            'Custom real-time dashboard design',
            'Revenue & expense tracking visuals',
            'Cash flow monitoring charts',
            'Profitability & margin analysis',
            'Multi-branch/department views',
            'Mobile-friendly access',
            'Automated daily/weekly/monthly reports',
            'Budget vs Actual comparison charts',
            'Trend analysis & forecasting visuals',
            'Role-based dashboard access control',
        ],
        'benefits': [
            {'icon': 'fas fa-eye', 'title': 'Instant Visibility', 'text': 'See your entire financial health at a glance — revenue, expenses, margins, and cash in one place.'},
            {'icon': 'fas fa-mobile-alt', 'title': 'Access Anywhere', 'text': 'Check your business performance from your phone, tablet, or laptop — anytime, anywhere.'},
            {'icon': 'fas fa-bolt', 'title': 'Faster Decisions', 'text': 'No more waiting for month-end reports — make data-driven decisions in real-time.'},
            {'icon': 'fas fa-sitemap', 'title': 'Multi-Level Views', 'text': 'From company-wide overview to department-level details with drill-down capability.'},
        ],
        'why_it_matters': 'In today\'s fast-paced business environment, decisions can\'t wait for monthly reports. Finance dashboards give you the power to monitor your business health 24/7, spot trends early, identify problems before they escalate, and communicate financial performance clearly to all stakeholders.',
        'ideal_for': [
            {'icon': 'fas fa-user-tie', 'text': 'Business owners wanting real-time visibility'},
            {'icon': 'fas fa-building', 'text': 'CFOs managing multiple departments'},
            {'icon': 'fas fa-digital-tachograph', 'text': 'Companies going digital with finance'},
            {'icon': 'fas fa-chart-pie', 'text': 'Data-driven decision makers'},
        ],
        'process': [
            {'step': 'Requirement Gathering', 'text': 'Understand what metrics matter most to your business and stakeholders.'},
            {'step': 'Data Mapping', 'text': 'Connect your accounting software, ERPs, and data sources.'},
            {'step': 'Dashboard Design', 'text': 'Build visually appealing, easy-to-read dashboards with drill-down capability.'},
            {'step': 'Testing & Training', 'text': 'User testing, feedback incorporation, and team training.'},
            {'step': 'Go Live & Support', 'text': 'Launch dashboards with ongoing support and periodic enhancements.'},
        ],
        'faqs': [
            {'q': 'Which accounting software do your dashboards connect with?', 'a': 'We integrate with Tally, Zoho Books, QuickBooks, Busy, and can also pull data from Excel/Google Sheets.'},
            {'q': 'Can I access the dashboard on my mobile phone?', 'a': 'Yes! All our dashboards are fully responsive and work beautifully on mobile, tablet, and desktop.'},
            {'q': 'How long does it take to set up a dashboard?', 'a': 'Basic dashboards can be ready in 1-2 weeks. Complex multi-source dashboards may take 3-4 weeks.'},
            {'q': 'Can different team members see different data?', 'a': 'Absolutely! We implement role-based access so each person sees only the data relevant to their role.'},
        ],
    },
    'ar-ap-management': {
        'icon': 'fas fa-exchange-alt',
        'color': '#ec4899',
        'gradient': 'linear-gradient(135deg, #ec4899, #db2777)',
        'title': 'AR & AP Management',
        'tagline': 'Collect Faster, Pay Smarter',
        'short_desc': 'Efficient accounts receivable and payable management.',
        'desc': 'Efficient accounts receivable and payable management to keep your cash flow healthy and your business relationships strong. We streamline your entire billing cycle — from invoice generation to payment collection — and optimize your vendor payment schedules to take advantage of early payment discounts while maintaining strong supplier relationships. Our systematic approach reduces your Days Sales Outstanding (DSO), minimizes bad debts, and ensures you never miss a payment deadline. We implement automated reminders, aging analysis, and escalation procedures that recover outstanding payments faster without damaging client relationships.',
        'highlights': [
            {'number': '60%', 'label': 'DSO Reduction'},
            {'number': '5L+', 'label': 'Cash Recovered Monthly'},
            {'number': '95%', 'label': 'Collection Rate'},
            {'number': '300+', 'label': 'Accounts Managed'},
        ],
        'features': [
            'Invoice tracking & follow-up system',
            'Aging analysis & collection strategy',
            'Vendor payment scheduling',
            'Early payment discount optimization',
            'Reconciliation & dispute management',
            'Credit policy design',
            'Automated payment reminders',
            'Bad debt analysis & write-off management',
            'Supplier relationship optimization',
            'DSO & DPO improvement strategies',
        ],
        'benefits': [
            {'icon': 'fas fa-funnel-dollar', 'title': 'Unlock Hidden Cash', 'text': 'Recover lakhs stuck in overdue receivables and optimize your entire cash conversion cycle.'},
            {'icon': 'fas fa-clock', 'title': 'Never Miss Deadlines', 'text': 'Automated reminders and scheduling ensure on-time payments and collections every time.'},
            {'icon': 'fas fa-handshake', 'title': 'Stronger Relationships', 'text': 'Professional follow-up systems that recover money without damaging business relationships.'},
            {'icon': 'fas fa-percentage', 'title': 'Save on Discounts', 'text': 'Strategic payment scheduling captures early payment discounts from vendors.'},
        ],
        'why_it_matters': 'Poor AR management means money stuck with customers for too long. Poor AP management means strained supplier relationships and missed discounts. Together, they directly impact your working capital, cash flow, and ultimately your ability to invest in growth. Efficient AR/AP management can unlock lakhs of hidden cash within your existing operations.',
        'ideal_for': [
            {'icon': 'fas fa-store', 'text': 'Trading & wholesale businesses'},
            {'icon': 'fas fa-redo', 'text': 'Companies with recurring invoicing'},
            {'icon': 'fas fa-industry', 'text': 'Manufacturing with multiple vendors'},
            {'icon': 'fas fa-money-bill-wave', 'text': 'Profitable but cash-strapped businesses'},
        ],
        'process': [
            {'step': 'Current State Audit', 'text': 'Analyze your existing AR/AP processes, aging reports, and collection rates.'},
            {'step': 'Policy Design', 'text': 'Create credit policies, payment terms, and escalation procedures.'},
            {'step': 'System Setup', 'text': 'Implement tracking tools, automated reminders, and reconciliation processes.'},
            {'step': 'Team Training', 'text': 'Train your accounts team on new workflows and collection techniques.'},
            {'step': 'Monitor & Improve', 'text': 'Track DSO/DPO trends and continuously optimize for better results.'},
        ],
        'faqs': [
            {'q': 'How much can AR/AP optimization actually save?', 'a': 'Most businesses recover 15-30% more cash within the first quarter by reducing DSO and capturing vendor discounts.'},
            {'q': 'Will aggressive collection hurt customer relationships?', 'a': 'Our approach is professional and diplomatic — structured follow-ups that maintain relationships while ensuring timely payments.'},
            {'q': 'Can you handle disputed invoices?', 'a': 'Yes, we set up dispute resolution workflows that track, escalate, and resolve invoice disputes systematically.'},
            {'q': 'Do you manage vendor negotiations?', 'a': 'We assist with negotiating better payment terms, early payment discounts, and credit terms with your key suppliers.'},
        ],
    },
    'business-health-checkup': {
        'icon': 'fas fa-heartbeat',
        'color': '#14b8a6',
        'gradient': 'linear-gradient(135deg, #14b8a6, #0d9488)',
        'title': 'Business Health Checkup',
        'tagline': 'Diagnose. Optimize. Thrive.',
        'short_desc': 'Comprehensive assessment of your business\'s financial wellness.',
        'desc': 'Comprehensive assessment of your business\'s financial wellness — think of it as a complete diagnostic test for your company. We go beyond surface-level numbers to analyze the fundamental health of your business across all financial dimensions. Our expert team examines your profitability trends, liquidity position, debt structure, operational efficiency, and growth trajectory using 50+ financial parameters. Just like a medical checkup catches health issues before they become serious, our business health checkup identifies financial red flags early, giving you time to course-correct. You receive a detailed report card with clear ratings, actionable insights, and a prioritized improvement roadmap.',
        'highlights': [
            {'number': '50+', 'label': 'Parameters Checked'},
            {'number': '250+', 'label': 'Checkups Completed'},
            {'number': '85%', 'label': 'Issues Caught Early'},
            {'number': '3x', 'label': 'ROI on Improvements'},
        ],
        'features': [
            'Complete financial health assessment',
            'Ratio analysis & benchmarking',
            'Profitability & growth trend review',
            'Risk exposure evaluation',
            'Operational efficiency audit',
            'Actionable improvement roadmap',
            '50+ financial parameter analysis',
            'Industry benchmarking comparison',
            'SWOT analysis from financial perspective',
            'Quarterly health tracking & monitoring',
        ],
        'benefits': [
            {'icon': 'fas fa-stethoscope', 'title': 'Complete Diagnosis', 'text': '50+ parameters analyzed across profitability, liquidity, solvency, and operational efficiency.'},
            {'icon': 'fas fa-flag', 'title': 'Red Flag Detection', 'text': 'Catch declining margins, rising debt ratios, and working capital issues before they become critical.'},
            {'icon': 'fas fa-map-signs', 'title': 'Clear Roadmap', 'text': 'Prioritized action plan with quick wins and long-term strategies for improvement.'},
            {'icon': 'fas fa-balance-scale', 'title': 'Industry Benchmarking', 'text': 'See how you compare against industry standards and competitors in your segment.'},
        ],
        'why_it_matters': 'Most business owners know their top-line revenue but have limited visibility into the true health of their business. Hidden issues like declining margins, increasing debt ratios, or deteriorating working capital can silently erode your business value. A regular health checkup catches these issues early and keeps your business in peak financial condition.',
        'ideal_for': [
            {'icon': 'fas fa-calendar-check', 'text': 'Businesses operating for 2+ years'},
            {'icon': 'fas fa-pause-circle', 'text': 'Companies with stagnant growth'},
            {'icon': 'fas fa-hand-holding-usd', 'text': 'Businesses preparing for investment'},
            {'icon': 'fas fa-search', 'text': 'Owners wanting unbiased assessment'},
        ],
        'process': [
            {'step': 'Data Collection', 'text': 'Gather financial statements, reports, and operational data for analysis.'},
            {'step': 'Comprehensive Analysis', 'text': 'Run 50+ parameter checks across profitability, liquidity, solvency, and efficiency.'},
            {'step': 'Benchmarking', 'text': 'Compare your performance against industry standards and competitors.'},
            {'step': 'Report Card', 'text': 'Deliver a detailed health report with ratings, insights, and red flags.'},
            {'step': 'Action Plan', 'text': 'Provide a prioritized roadmap with quick wins and long-term improvements.'},
        ],
        'faqs': [
            {'q': 'How is this different from a regular audit?', 'a': 'An audit checks compliance. Our health checkup analyzes business performance, efficiency, and growth potential — it\'s diagnostic, not just verification.'},
            {'q': 'What data do you need from us?', 'a': 'Last 2-3 years of financial statements, bank statements, key operational reports, and access to your accounting software.'},
            {'q': 'How long does the checkup take?', 'a': 'The full analysis takes 2-3 weeks, with a preliminary findings report within the first week.'},
            {'q': 'Do you provide ongoing monitoring after the checkup?', 'a': 'Yes! We offer quarterly tracking packages to monitor improvement and catch new issues early.'},
        ],
    },
    'ipo-advisory': {
        'icon': 'fas fa-rocket',
        'color': '#d4af37',
        'gradient': 'linear-gradient(135deg, #d4af37, #b8941f)',
        'title': 'IPO Advisory',
        'tagline': 'From Private to Public — We Guide Every Step',
        'short_desc': 'Expert guidance to prepare your company for an Initial Public Offering.',
        'desc': 'Expert guidance to prepare your company for an Initial Public Offering — one of the most transformative events in a company\'s journey. From the initial readiness assessment to post-listing compliance, we provide end-to-end support that covers every aspect of the IPO process. Our experienced team has deep knowledge of SEBI regulations, stock exchange requirements, and investor expectations. We help you restructure your finances, clean up your books, establish corporate governance frameworks, and build the financial narrative that attracts investors. Going public is a complex, multi-year process — we ensure you are fully prepared at every stage, reducing delays, avoiding regulatory issues, and maximizing your valuation.',
        'highlights': [
            {'number': '15+', 'label': 'IPOs Supported'},
            {'number': '500Cr+', 'label': 'Capital Raised'},
            {'number': '100%', 'label': 'SEBI Compliance'},
            {'number': '2x', 'label': 'Avg. Valuation Uplift'},
        ],
        'features': [
            'IPO readiness assessment',
            'Financial restructuring & cleanup',
            'SEBI compliance preparation',
            'Valuation & pricing strategy',
            'Due diligence coordination',
            'Post-IPO compliance support',
            'Corporate governance framework setup',
            'Prospectus & DRHP preparation support',
            'Investor presentation & roadshow prep',
            'Internal systems upgrade for listed company requirements',
        ],
        'benefits': [
            {'icon': 'fas fa-gem', 'title': 'Maximum Valuation', 'text': 'Strategic positioning and financial cleanup that consistently delivers higher IPO valuations.'},
            {'icon': 'fas fa-gavel', 'title': 'Full SEBI Compliance', 'text': 'Navigate complex regulatory requirements with zero compliance failures or listing delays.'},
            {'icon': 'fas fa-users', 'title': 'Investor Confidence', 'text': 'Build a compelling financial narrative and governance framework that attracts institutional investors.'},
            {'icon': 'fas fa-life-ring', 'title': 'Post-IPO Support', 'text': 'Ongoing compliance, reporting, and investor relations support even after listing.'},
        ],
        'why_it_matters': 'An IPO is not just about raising capital — it\'s about building credibility, unlocking growth, and creating value for all stakeholders. However, poor preparation can lead to regulatory delays, lower valuations, or even failed listings. Companies that invest in thorough IPO preparation consistently achieve better valuations, smoother listings, and stronger post-IPO performance.',
        'ideal_for': [
            {'icon': 'fas fa-rupee-sign', 'text': 'Companies with Rs.50 Cr+ annual revenue'},
            {'icon': 'fas fa-calendar', 'text': 'Businesses planning IPO in 1-3 years'},
            {'icon': 'fas fa-unlock-alt', 'text': 'Promoters unlocking company value'},
            {'icon': 'fas fa-landmark', 'text': 'Companies seeking public market access'},
        ],
        'process': [
            {'step': 'Readiness Assessment', 'text': 'Evaluate your company\'s IPO readiness across financial, legal, and operational dimensions.'},
            {'step': 'Financial Restructuring', 'text': 'Clean up books, resolve contingencies, and align financials with listing requirements.'},
            {'step': 'Governance Setup', 'text': 'Establish board committees, compliance frameworks, and corporate governance policies.'},
            {'step': 'Documentation', 'text': 'Support DRHP preparation, prospectus drafting, and regulatory filings.'},
            {'step': 'Post-IPO Support', 'text': 'Ongoing compliance, quarterly reporting, and investor relations support.'},
        ],
        'faqs': [
            {'q': 'When should we start preparing for an IPO?', 'a': 'Ideally 2-3 years before the planned listing date. Early preparation ensures clean financials and strong governance.'},
            {'q': 'What is the minimum company size for an IPO?', 'a': 'For SME IPO, Rs.1-25 Cr net worth. For Main Board, Rs.25 Cr+ net worth. We help assess your specific eligibility.'},
            {'q': 'Do you help with SME IPOs as well?', 'a': 'Yes! We have extensive experience with both SME platform listings and Main Board IPOs.'},
            {'q': 'What is the typical timeline for an IPO process?', 'a': 'From start to listing, it typically takes 12-18 months including preparation, regulatory approvals, and marketing.'},
        ],
    },
}

SERVICE_SLUGS = list(SERVICES_DATA.keys())


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def benefits(request):
    return render(request, 'benefits.html')


def services(request):
    return render(request, 'services.html')


def service_detail(request, slug):
    service = SERVICES_DATA.get(slug)
    if not service:
        raise Http404("Service not found")

    # Find prev/next services for navigation
    idx = SERVICE_SLUGS.index(slug)
    prev_service = None
    next_service = None
    if idx > 0:
        prev_slug = SERVICE_SLUGS[idx - 1]
        prev_service = {'slug': prev_slug, 'title': SERVICES_DATA[prev_slug]['title']}
    if idx < len(SERVICE_SLUGS) - 1:
        next_slug = SERVICE_SLUGS[idx + 1]
        next_service = {'slug': next_slug, 'title': SERVICES_DATA[next_slug]['title']}

    return render(request, 'service_detail.html', {
        'service': service,
        'slug': slug,
        'prev_service': prev_service,
        'next_service': next_service,
    })


def process(request):
    return render(request, 'process.html')


def contact(request):
    return render(request, 'contact.html')


def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        company_name = request.POST.get('company_name', '').strip()
        service_interested = request.POST.get('service_interested', '').strip()
        budget_range = request.POST.get('budget_range', '').strip()
        urgency = request.POST.get('urgency', '').strip()
        message = request.POST.get('message', '').strip()

        if name and email and message:
            ContactMessage.objects.create(
                name=name, email=email, phone=phone,
                company_name=company_name,
                service_interested=service_interested,
                budget_range=budget_range,
                urgency=urgency,
                message=message,
            )

            email_subject = f'New Contact Inquiry from {name}'
            email_body = (
                f'New contact form submission received.\n\n'
                f'Name: {name}\n'
                f'Email: {email}\n'
                f'Phone: {phone or "N/A"}\n'
                f'Company: {company_name or "N/A"}\n'
                f'Service Interested: {service_interested or "N/A"}\n'
                f'Budget Range: {budget_range or "N/A"}\n'
                f'Timeline: {urgency or "N/A"}\n\n'
                f'Message:\n{message}\n'
            )
            try:
                send_mail(
                    subject=email_subject,
                    message=email_body,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_NOTIFICATION_EMAIL],
                    fail_silently=True,
                )
            except Exception:
                pass

            messages.success(request, 'Thank you! Your message has been sent. We will get back to you shortly.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all required fields.')

    return redirect('contact')


def team(request):
    return render(request, 'team.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')


def terms_of_service(request):
    return render(request, 'terms_of_service.html')


def page_not_found(request, exception):
    return render(request, '404.html', status=404)


def newsletter_subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('newsletter_email', '').strip()
        if email:
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email)
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            else:
                messages.info(request, 'You are already subscribed to our newsletter.')
        else:
            messages.error(request, 'Please enter a valid email address.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))
