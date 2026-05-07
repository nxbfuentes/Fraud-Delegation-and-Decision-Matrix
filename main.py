import matplotlib.pyplot as plt
import numpy as np

# Create a simple 3x3 Risk Matrix for the Fraud project
# 0=Green, 1=Amber, 2=Red, 3=DarkRed
risk_data = np.array([
    [0, 1, 2],  # Low Likelihood
    [1, 2, 3],  # Medium Likelihood
    [2, 3, 3]   # High Likelihood
])

fig, ax = plt.subplots(figsize=(8, 6))
cmap = plt.cm.get_cmap('RdYlGn_r') # Red to Green reversed
cax = ax.matshow(risk_data, cmap=cmap)

# Labels
ax.set_xticks([0, 1, 2])
ax.set_yticks([0, 1, 2])
ax.set_xticklabels(['Low', 'Medium', 'High'])
ax.set_yticklabels(['High', 'Medium', 'Low']) # Inverted for Matrix look

ax.set_xlabel('Transaction Complexity / Scam Likelihood', fontweight='bold')
ax.set_ylabel('Potential Financial Impact', fontweight='bold')

# Annotations
labels = [
    ['Med Risk\n(Fraud Bureau)', 'High Risk\n(Fraud Team)', 'Extreme Risk\n(Fraud Team)'],
    ['Low Risk\n(Senior CC)', 'Med Risk\n(Fraud Bureau)', 'High Risk\n(Fraud Team)'],
    ['Low Risk\n(Senior CC)', 'Low Risk\n(Senior CC)', 'Med Risk\n(Fraud Bureau)']
]

for i in range(3):
    for j in range(3):
        ax.text(j, i, labels[i][j], ha='center', va='center', fontsize=9, fontweight='bold')

plt.title('Fraud Escalation Risk Matrix', fontsize=14, fontweight='bold', pad=20)
plt.savefig('fraud_risk_matrix.png', bbox_inches='tight')
print("Matrix diagram generated.")
