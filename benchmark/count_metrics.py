from sklearn.metrics import mean_squared_error


def count_rmse(true, prediction):
    true_non_null = true != 0

    user_non_null = true[true_non_null]
    fitted_prediction = prediction[true_non_null]

    rmse = mean_squared_error(user_non_null, fitted_prediction, squared=False)

    return rmse


def count_rmse_on_dataset(model, data):
    sum_rmse = 0
    num_predictions = 0

    for id, sample in enumerate(data):
        if sum(sample) == 0:
            continue

        pred = model.predict(id)
        rmse = count_rmse(sample, pred)

        sum_rmse += rmse
        num_predictions += 1

    rmse = sum_rmse / num_predictions

    return rmse
