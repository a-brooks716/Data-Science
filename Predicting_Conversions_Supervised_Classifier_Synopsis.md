# Project Proposal: Predicting Conversions with Supervised Classification

## Objective

The goal of this project is to develop a supervised classification model that can accurately predict customer conversions based on demographics and other available data from the coverage team in the insurance vertical. By leveraging insights from user characteristics, I aim to create a predictive tool that will empower our marketing and sales teams to prioritize high-conversion leads. 

From talks with the conversion team, this information would lead to testing shorter funnels for those with a high probability of converting rather than the typical funnel they are given now. In theory, this would improve overall efficiency and increase revenue. The ability to anticipate conversion likelihood will not only streamline targeting efforts but also help allocate resources to the most promising leads.

## Data Preprocessing and Feature Engineering 

A significant portion of this project revolves around effectively preprocessing the data for optimal model performance. The data we're working with has a mix of structured and unstructured fields, including JSON columns that are integrated from the Quadrant profile for specific user data (policy, vehicles, and incidents, among others.) 

**PII was scrubbed prior to extraction.** 

One of the main challenges has been converting these multi-nested JSON fields into a flat format that can be analyzed effectively. Then combine the data frames into one large dataset before beginning to determine what columns are redundant or could possibly skew the model. 

Another challenge was handling non-numeric data, from the initial view, most of the data is categorical and not numerical which poses a problem for the models I’ve selected. I opted for one-hot encoding instead of ordinal encoding where the model could misinterpret the extra dimensionality of the ordered values (1,2,3, etc.) and confuse the machine. 

## Models I Will Be Using

For this project, I will be using three different models to determine which one best suits our needs and see various outputs:

1. Logistic Regression: This model serves as a baseline to establish the performance of a simple linear classifier. I felt this would provide a straightforward interpretability of how each feature affects conversion.

2. Random Forest: Given the range of categorical and numerical features in our dataset, I felt this model might also be beneficial as it can handle them more effectively without extensive scaling or transformations.

3. Gradient Boosting: Finally, I wanted to enhance predictive power, so I felt employing Gradient Boosting would be a value add. This approach will help to fine-tune the model and increase its ability to identify subtle relationships within the data, often leading to improved accuracy over Random Forest and Logistic Regression.

## Goals

The primary goal of this project is to develop a highly accurate model that can identify the likelihood of a lead converting, based on their demographic and historical data. From a business perspective, this model will help us prioritize leads, allowing the sales team to focus on those that are most likely to convert. This targeted approach is expected to drive more efficient use of marketing dollars, lower customer acquisition costs, and boost revenue growth. 

Also, insights pulled from the model could inform strategic decisions, such as refining marketing messaging or adjusting the segmentation of campaigns to align more closely with high-converting customer profiles.

By effectively predicting conversions, we can create a more personalized customer journey, improve customer satisfaction, and ultimately enhance the company's profitability and competitive position in the market.
