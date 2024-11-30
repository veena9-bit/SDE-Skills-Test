{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "570b0b2b-c7d9-4873-8204-a417b81d7169",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_csv(file_path):\n",
    "    \"\"\"\n",
    "    Load a CSV file into a Pandas DataFrame.\n",
    "\n",
    "    Parameters:\n",
    "    file_path (str): The path to the CSV file.\n",
    "\n",
    "    Returns:\n",
    "    pd.DataFrame: The loaded DataFrame.\n",
    "    \"\"\"\n",
    "    try:\n",
    "        # Read the CSV file into a DataFrame\n",
    "        df = pd.read_csv(file_path)\n",
    "        return df\n",
    "    except Exception as e:\n",
    "        print(f\"Error loading CSV file: {e}\")\n",
    "        return None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "23dcdbed-29b2-47bd-afcf-784c6879afba",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
