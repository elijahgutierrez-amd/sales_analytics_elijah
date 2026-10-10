# Part H: Ethics, Privacy, and Emerging Tech Reflection

### 1. Data Privacy Act of 2012 Compliance & Masking
Under the Philippine Data Privacy Act of 2012 (DPA), the seller must establish a clear lawful basis—such as obtaining explicit user consent or proving legitimate business interest—and enforce strict data minimization before processing customer data. Personally Identifiable Information (PII) like names, phone numbers, and full delivery addresses must be removed or masked using cryptographic hashing (e.g., SHA-256) or tokenization prior to analytics. In this dataset, raw customer names, phone numbers, and exact street addresses would be removed, while broad geographic indicators like `region` and `province` are retained to maintain analytical value without compromising individual privacy.

### 2. Ethical Dilemmas of Restricting COD
Completely eliminating Cash on Delivery (COD) would disproportionately hurt unbanked consumers, students, and low-income buyers in rural regions who lack access to credit cards or e-wallets like GCash and Maya. To make an ethical and commercially sound decision, the seller should avoid blanket bans and instead use risk-based filtering—such as requiring digital prepayment only for high-value items, flagging high-risk delivery addresses, or offering small promotional discounts to incentivize digital payments while keeping COD accessible for lower-value transactions.

### 3. The 5 Vs of Big Data in the 11.11 Analytics Lab
* **Volume:** Represented by processing a 1,000,000-row transaction dataset (~80 MB raw CSV) using distributed memory allocation in PySpark rather than standard manual spreadsheet processing.
* **Velocity:** Evidenced by analyzing extreme transaction rate spikes during specific peak hours (e.g., 12:00–1:00 AM and 8:00–10:00 PM on November 11), mimicking real-time event streaming during flash sales.

### 4. Emerging Tech: IoT Integration & Drawbacks
IoT sensors embedded in delivery vehicle GPS trackers and smart parcel lockers can introduce real-time telemetry data—such as exact delivery timestamps, ambient transit temperatures, and precise package locations—to enrich order fulfillment analysis. However, a major drawback is the high capital cost required for IoT hardware deployment and maintenance, alongside network bandwidth constraints and data dropouts across remote regions in the Philippines.
