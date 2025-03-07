{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "13097de2-ecdd-4a4c-b1ba-e01235e0b5f7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-03-07 22:45:00.934 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "ename": "RuntimeError",
     "evalue": "Runtime hasn't been created!",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\streamlit\\elements\\lib\\image_utils.py:286\u001b[0m, in \u001b[0;36mimage_to_url\u001b[1;34m(image, width, clamp, channels, output_format, image_id)\u001b[0m\n\u001b[0;32m    285\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 286\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\u001b[43mimage\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mrb\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[0;32m    287\u001b[0m         image_data \u001b[38;5;241m=\u001b[39m f\u001b[38;5;241m.\u001b[39mread()\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'BikeRental.png'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[27], line 72\u001b[0m\n\u001b[0;32m     68\u001b[0m max_date \u001b[38;5;241m=\u001b[39m day_clean_df[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdteday\u001b[39m\u001b[38;5;124m\"\u001b[39m]\u001b[38;5;241m.\u001b[39mmax()\n\u001b[0;32m     70\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m st\u001b[38;5;241m.\u001b[39msidebar:\n\u001b[0;32m     71\u001b[0m     \u001b[38;5;66;03m# Menambahkan logo \u001b[39;00m\n\u001b[1;32m---> 72\u001b[0m     \u001b[43mst\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mimage\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mBikeRental.png\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m     74\u001b[0m     \u001b[38;5;66;03m# Mengambil start_date & end_date dari date_input\u001b[39;00m\n\u001b[0;32m     75\u001b[0m     start_date, end_date \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mdate_input(\n\u001b[0;32m     76\u001b[0m         label\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mRentang Waktu\u001b[39m\u001b[38;5;124m'\u001b[39m,\n\u001b[0;32m     77\u001b[0m         min_value\u001b[38;5;241m=\u001b[39mmin_date,\n\u001b[0;32m     78\u001b[0m         max_value\u001b[38;5;241m=\u001b[39mmax_date,\n\u001b[0;32m     79\u001b[0m         value\u001b[38;5;241m=\u001b[39m[min_date, max_date]\n\u001b[0;32m     80\u001b[0m     )\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\streamlit\\runtime\\metrics_util.py:410\u001b[0m, in \u001b[0;36mgather_metrics.<locals>.wrapped_func\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    408\u001b[0m         _LOGGER\u001b[38;5;241m.\u001b[39mdebug(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mFailed to collect command telemetry\u001b[39m\u001b[38;5;124m\"\u001b[39m, exc_info\u001b[38;5;241m=\u001b[39mex)\n\u001b[0;32m    409\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[1;32m--> 410\u001b[0m     result \u001b[38;5;241m=\u001b[39m \u001b[43mnon_optional_func\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43margs\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[38;5;241;43m*\u001b[39;49m\u001b[43mkwargs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    411\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m RerunException \u001b[38;5;28;01mas\u001b[39;00m ex:\n\u001b[0;32m    412\u001b[0m     \u001b[38;5;66;03m# Duplicated from below, because static analysis tools get confused\u001b[39;00m\n\u001b[0;32m    413\u001b[0m     \u001b[38;5;66;03m# by deferring the rethrow.\u001b[39;00m\n\u001b[0;32m    414\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m tracking_activated \u001b[38;5;129;01mand\u001b[39;00m command_telemetry:\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\streamlit\\elements\\image.py:181\u001b[0m, in \u001b[0;36mImageMixin.image\u001b[1;34m(self, image, caption, width, use_column_width, clamp, channels, output_format, use_container_width)\u001b[0m\n\u001b[0;32m    178\u001b[0m         image_width \u001b[38;5;241m=\u001b[39m WidthBehavior\u001b[38;5;241m.\u001b[39mMIN_IMAGE_OR_CONTAINER\n\u001b[0;32m    180\u001b[0m image_list_proto \u001b[38;5;241m=\u001b[39m ImageListProto()\n\u001b[1;32m--> 181\u001b[0m \u001b[43mmarshall_images\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    182\u001b[0m \u001b[43m    \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdg\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_get_delta_path_str\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    183\u001b[0m \u001b[43m    \u001b[49m\u001b[43mimage\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    184\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcaption\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    185\u001b[0m \u001b[43m    \u001b[49m\u001b[43mimage_width\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    186\u001b[0m \u001b[43m    \u001b[49m\u001b[43mimage_list_proto\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    187\u001b[0m \u001b[43m    \u001b[49m\u001b[43mclamp\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    188\u001b[0m \u001b[43m    \u001b[49m\u001b[43mchannels\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    189\u001b[0m \u001b[43m    \u001b[49m\u001b[43moutput_format\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    190\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    191\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mdg\u001b[38;5;241m.\u001b[39m_enqueue(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mimgs\u001b[39m\u001b[38;5;124m\"\u001b[39m, image_list_proto)\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\streamlit\\elements\\lib\\image_utils.py:439\u001b[0m, in \u001b[0;36mmarshall_images\u001b[1;34m(coordinates, image, caption, width, proto_imgs, clamp, channels, output_format)\u001b[0m\n\u001b[0;32m    435\u001b[0m \u001b[38;5;66;03m# We use the index of the image in the input image list to identify this image inside\u001b[39;00m\n\u001b[0;32m    436\u001b[0m \u001b[38;5;66;03m# MediaFileManager. For this, we just add the index to the image's \"coordinates\".\u001b[39;00m\n\u001b[0;32m    437\u001b[0m image_id \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m-\u001b[39m\u001b[38;5;132;01m%i\u001b[39;00m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m%\u001b[39m (coordinates, coord_suffix)\n\u001b[1;32m--> 439\u001b[0m proto_img\u001b[38;5;241m.\u001b[39murl \u001b[38;5;241m=\u001b[39m \u001b[43mimage_to_url\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    440\u001b[0m \u001b[43m    \u001b[49m\u001b[43mimage\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mwidth\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mclamp\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mchannels\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43moutput_format\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mimage_id\u001b[49m\n\u001b[0;32m    441\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\streamlit\\elements\\lib\\image_utils.py:298\u001b[0m, in \u001b[0;36mimage_to_url\u001b[1;34m(image, width, clamp, channels, output_format, image_id)\u001b[0m\n\u001b[0;32m    295\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m mimetype \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    296\u001b[0m     mimetype \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mapplication/octet-stream\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m--> 298\u001b[0m url \u001b[38;5;241m=\u001b[39m \u001b[43mruntime\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget_instance\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\u001b[38;5;241m.\u001b[39mmedia_file_mgr\u001b[38;5;241m.\u001b[39madd(image, mimetype, image_id)\n\u001b[0;32m    299\u001b[0m caching\u001b[38;5;241m.\u001b[39msave_media_data(image, mimetype, image_id)\n\u001b[0;32m    300\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m url\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\streamlit\\runtime\\__init__.py:28\u001b[0m, in \u001b[0;36mget_instance\u001b[1;34m()\u001b[0m\n\u001b[0;32m     24\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mget_instance\u001b[39m() \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m Runtime:\n\u001b[0;32m     25\u001b[0m \u001b[38;5;250m    \u001b[39m\u001b[38;5;124;03m\"\"\"Return the singleton Runtime instance. Raise an Error if the\u001b[39;00m\n\u001b[0;32m     26\u001b[0m \u001b[38;5;124;03m    Runtime hasn't been created yet.\u001b[39;00m\n\u001b[0;32m     27\u001b[0m \u001b[38;5;124;03m    \"\"\"\u001b[39;00m\n\u001b[1;32m---> 28\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mRuntime\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43minstance\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\streamlit\\runtime\\runtime.py:163\u001b[0m, in \u001b[0;36mRuntime.instance\u001b[1;34m(cls)\u001b[0m\n\u001b[0;32m    159\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"Return the singleton Runtime instance. Raise an Error if the\u001b[39;00m\n\u001b[0;32m    160\u001b[0m \u001b[38;5;124;03mRuntime hasn't been created yet.\u001b[39;00m\n\u001b[0;32m    161\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    162\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mcls\u001b[39m\u001b[38;5;241m.\u001b[39m_instance \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m--> 163\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mRuntime hasn\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt been created!\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m    164\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mcls\u001b[39m\u001b[38;5;241m.\u001b[39m_instance\n",
      "\u001b[1;31mRuntimeError\u001b[0m: Runtime hasn't been created!"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import streamlit as st\n",
    "import datetime\n",
    "\n",
    "sns.set(style='whitegrid') \n",
    "plt.style.use('ggplot')\n",
    "# Helper function yang dibutuhkan untuk menyiapkan berbagai dataframe\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c4b7ca06-5832-4612-a019-11ce064ef434",
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
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
