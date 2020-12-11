# Plan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the plan | [optional] 
**customer** | [**PlanCustomer**](PlanCustomer.md) |  | [optional] 
**product** | [**PlanProduct**](PlanProduct.md) |  | [optional] 
**scheme** | [**PlanScheme**](PlanScheme.md) |  | [optional] 
**enrolled_on** | **datetime** | Time when customer enrolled on the plan | [optional] 
**plan_value** | **int** | Total price of the plan, to be paid by the customer | [optional] 
**instalment_value** | **int** | Value of each instalment to be paid by the customer | [optional] 
**total_paid_value** | **int** | Total amount paid by the customer towards the plan till date | [optional] 
**completed_instalments** | **int** | Instalments paid by customer till date | [optional] 
**next_instalment_date** | **date** | Due date for the upcoming instalment of the plan | [optional] 
**plan_maturity_date** | **date** | Date on which the plan is expected to mature | [optional] 
**total_expected_redemption_value** | **int** | Total amount expected to be redeemed by the customer at the end of the plan | [optional] 
**current_redemption_value** | **int** | Total amount that can be redeemed by the customer by closing the plan today | [optional] 
**current_cancellation_value** | **int** | Total amount that is paid back to customer if the plan is cancelled today | [optional] 
**last_instalment_paid_on** | **datetime** | Timestamp of last paid instalment | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


